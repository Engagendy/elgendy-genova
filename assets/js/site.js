(() => {
  const root = document.documentElement;
  const rtl = () => root.dir === 'rtl';

  // Theme (light default, dark optional). The initial class is set inline in <head>.
  const themeBtn = document.getElementById('themeToggle');
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  function setTheme(dark) {
    if (dark) root.dataset.theme = 'dark';
    else delete root.dataset.theme;
    themeBtn?.setAttribute('aria-pressed', String(dark));
    themeMeta?.setAttribute('content', dark ? '#0e0d0b' : '#faf6ef');
    try { localStorage.setItem('elgendy-theme', dark ? 'dark' : 'light'); } catch (e) {}
  }
  themeBtn?.setAttribute('aria-pressed', String(root.dataset.theme === 'dark'));
  themeBtn?.addEventListener('click', () => setTheme(root.dataset.theme !== 'dark'));

  // Header state + mobile menu
  const header = document.getElementById('header');
  const onScroll = () => header.classList.toggle('is-solid', window.scrollY > 30);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  const toggle = header.querySelector('.menu-toggle');
  toggle?.addEventListener('click', () => {
    const open = header.classList.toggle('menu-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  header.querySelectorAll('.nav-links a').forEach((a) => a.addEventListener('click', () => {
    header.classList.remove('menu-open');
    toggle?.setAttribute('aria-expanded', 'false');
  }));

  // Tabs
  document.querySelectorAll('[role="tablist"]').forEach((list) => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];
    const select = (tab) => tabs.forEach((x) => {
      const on = x === tab;
      x.setAttribute('aria-selected', String(on));
      x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
    });
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', (e) => {
        const dir = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (!dir) return;
        const next = tabs[(i + (rtl() ? -dir : dir) + tabs.length) % tabs.length];
        select(next);
        next.focus();
      });
    });
  });

  // Galleries: filter + paging + lightbox
  const box = document.getElementById('lightbox');
  let lbList = [];
  let lbIndex = 0;

  function renderLightbox(rebuild) {
    const item = lbList[lbIndex];
    const img = box.querySelector('#lbImg');
    img.src = item.href;
    img.alt = item.querySelector('img').alt;
    box.querySelector('#lbTitle').textContent = item.dataset.label || '';
    box.querySelector('#lbCount').textContent = `${lbIndex + 1} / ${lbList.length}`;
    const thumbs = box.querySelector('#lbThumbs');
    if (rebuild) {
      thumbs.innerHTML = '';
      lbList.forEach((it, i) => {
        const b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', String(i + 1));
        b.innerHTML = `<img src="${it.querySelector('img').currentSrc || it.querySelector('img').src}" alt="" loading="lazy" decoding="async">`;
        b.addEventListener('click', () => { lbIndex = i; renderLightbox(false); });
        thumbs.appendChild(b);
      });
    }
    [...thumbs.children].forEach((b, i) => b.setAttribute('aria-current', String(i === lbIndex)));
    thumbs.children[lbIndex]?.scrollIntoView({ block: 'nearest', inline: 'center' });
  }

  function openLightbox(list, index) {
    lbList = list;
    lbIndex = index;
    box.classList.add('is-open');
    box.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    renderLightbox(true);
    box.querySelector('#lbClose').focus();
  }

  function closeLightbox() {
    box.classList.remove('is-open');
    box.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  const step = (dir) => {
    lbIndex = (lbIndex + dir + lbList.length) % lbList.length;
    renderLightbox(false);
  };

  if (box) {
    box.querySelector('#lbClose').addEventListener('click', closeLightbox);
    box.querySelector('#lbPrev').addEventListener('click', () => step(-1));
    box.querySelector('#lbNext').addEventListener('click', () => step(1));
    box.addEventListener('click', (e) => { if (e.target.classList.contains('lb-stage')) closeLightbox(); });
    document.addEventListener('keydown', (e) => {
      if (!box.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') step(rtl() ? 1 : -1);
      if (e.key === 'ArrowRight') step(rtl() ? -1 : 1);
    });
    let touchX = null;
    const stage = box.querySelector('.lb-stage');
    stage.addEventListener('touchstart', (e) => { touchX = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener('touchend', (e) => {
      if (touchX === null) return;
      const dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) step((dx < 0) !== rtl() ? 1 : -1);
      touchX = null;
    });
  }

  document.querySelectorAll('[data-gallery]').forEach((grid) => {
    const items = [...grid.querySelectorAll('.work')];
    const page = Number(grid.dataset.page) || Infinity;
    const filters = document.querySelector(`[data-filters="${grid.id}"]`);
    const more = document.querySelector(`[data-more="${grid.id}"]`);
    let filter = 'all';
    let shown = page;
    const matching = () => items.filter((it) => filter === 'all' || it.dataset.cat === filter);

    function render() {
      const list = matching();
      items.forEach((it) => it.classList.add('is-hidden'));
      list.slice(0, shown).forEach((it) => it.classList.remove('is-hidden'));
      if (more) more.hidden = shown >= list.length;
    }

    filters?.querySelectorAll('button').forEach((b) => b.addEventListener('click', () => {
      filter = b.dataset.filter;
      shown = page;
      filters.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
      render();
    }));
    more?.addEventListener('click', () => { shown += page; render(); });
    items.forEach((it) => it.addEventListener('click', (e) => {
      if (!box) return;
      e.preventDefault();
      const list = matching();
      openLightbox(list, list.indexOf(it));
    }));
    render();
  });

  // Quote form -> WhatsApp
  const form = document.getElementById('quoteForm');
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const lines = [form.dataset.intro];
    form.querySelectorAll('input, select, textarea').forEach((field) => {
      const label = form.querySelector(`label[for="${field.id}"]`)?.textContent.trim() || field.name;
      lines.push(`${label}: ${field.value.trim() || '-'}`);
    });
    const url = `https://wa.me/${form.dataset.phone}?text=${encodeURIComponent(lines.join('\n'))}`;
    window.open(url, '_blank', 'noopener');
  });

  // Reveal on scroll
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
