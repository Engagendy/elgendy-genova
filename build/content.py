"""All page copy for the El Gendy Genova site, in Arabic and English.

Edit text here, then run `python3 build/build.py` to regenerate the HTML pages.
"""

SITE = "https://engagendy.github.io/elgendy-genova"
BASE = "/elgendy-genova/"  # change to "/" when moving to a custom domain
PHONE = "201009455453"
PHONE_DISPLAY = "+20 100 945 5453"
EMAIL = "elgendykitchens@gmail.com"
FACEBOOK = "https://www.facebook.com/atceg"
UPDATED = "2026-10-06"

MAP_SHOWROOM = "https://www.google.com/maps/search/?api=1&query=%D8%B4%D8%A7%D8%B1%D8%B9%20%D8%A7%D9%84%D8%B3%D9%84%D8%A7%D8%A8%20%D8%A7%D9%84%D9%85%D9%86%D8%B5%D9%88%D8%B1%D8%A9"
MAP_FACTORY = "https://www.google.com/maps/search/?api=1&query=%D8%A7%D9%84%D8%A3%D9%85%D9%86%20%D8%A7%D9%84%D9%85%D8%B1%D9%83%D8%B2%D9%8A%20%D8%A7%D9%84%D9%85%D9%86%D8%B5%D9%88%D8%B1%D8%A9"

# Gallery categories (photo ids live in build/photos.json)
CATEGORIES = {
    "modern": {"ar": "مطابخ خشب مودرن", "en": "Modern wood kitchens"},
    "classic": {"ar": "مطابخ خشب كلاسيك", "en": "Classic wood kitchens"},
    "alukitchen": {"ar": "مطابخ ألوميتال", "en": "Aluminum kitchens"},
    "upvc": {"ar": "شبابيك UPVC", "en": "UPVC windows"},
    "aluwindow": {"ar": "شبابيك وواجهات ألوميتال", "en": "Aluminum windows & facades"},
    "doors": {"ar": "أبواب UPVC", "en": "UPVC doors"},
    "decor": {"ar": "ديكورات حوائط", "en": "Feature walls"},
    "details": {"ar": "تفاصيل وإكسسوارات", "en": "Details & fittings"},
}

UI = {
    "ar": {
        "brand": "الجندي جينوفا للمطابخ والشبابيك",
        "brandShort": "الجندي",
        "brandSub": "جينوفا · للمطابخ والشبابيك",
        "city": "المنصورة",
        "workBy": "من أعمال الجندي جينوفا بالمنصورة",
        "home": "الرئيسية",
        "navServices": "خدماتنا",
        "navGuide": "دليل الخامات",
        "navWorks": "أعمالنا",
        "navFaq": "أسئلة شائعة",
        "navContact": "تواصل معنا",
        "mainMenu": "القائمة الرئيسية",
        "menu": "القائمة",
        "darkMode": "الوضع الداكن",
        "langLabel": "اللغة",
        "callNow": "اتصل الآن",
        "whatsapp": "واتساب",
        "waMessage": "السلام عليكم، عايز أستفسر عن خدمة من الجندي جينوفا",
        "freeConsult": "احجز معاينة مجانية",
        "seeWorks": "شاهد أعمالنا",
        "learnMore": "اعرف التفاصيل ←",
        "allPhotos": "معرض الأعمال الكامل ←",
        "loadMore": "عرض المزيد",
        "moreOnFb": "كل الصور على فيسبوك",
        "all": "الكل",
        "close": "إغلاق",
        "prev": "السابق",
        "next": "التالي",
        "quoteTitle": "اطلب معاينة أو عرض سعر",
        "quoteLead": "املأ البيانات وهتتفتح رسالة واتساب جاهزة توصل لنا مباشرة.",
        "quoteIntro": "السلام عليكم، عايز معاينة / عرض سعر من الجندي جينوفا",
        "fName": "الاسم", "fNamePh": "اسمك",
        "fPhone": "رقم الموبايل",
        "fService": "نوع الشغل",
        "fArea": "المنطقة", "fAreaPh": "مثال: المنصورة - حي الجامعة",
        "fMsg": "تفاصيل", "fMsgPh": "المقاسات التقريبية، الألوان، أو أي فكرة في دماغك",
        "fMore": "أكثر من خدمة",
        "send": "إرسال على واتساب",
        "showroom": "المعرض",
        "showroomAddr": "المنصورة — آخر شارع سامية الجمل، شارع السلاب",
        "factory": "المصنع",
        "factoryAddr": "المنصورة — خلف الأمن المركزي",
        "reach": "كلّمنا",
        "openMap": "افتح على الخريطة ←",
        "chatWa": "ابدأ محادثة واتساب ←",
        "footerAbout": "مطابخ ألوميتال وخشب، شبابيك وأبواب UPVC وألوميتال، زجاج سيكوريت وديكورات حوائط — تصنيع وتركيب من مصنعنا في المنصورة.",
        "footerServices": "الخدمات",
        "footerLinks": "روابط",
        "footerContact": "تواصل",
        "footerCity": "المنصورة، الدقهلية، مصر",
        "tagline": "مصمَّم ليُبهر… ومصنوع ليدوم",
        "ctaTitle": "مهما كانت المساحة صغيرة… هنستغل كل سنتيمتر",
        "ctaLead": "ابعت صورة المكان ومقاسات تقريبية، ونرجعلك بتصوّر مبدئي وعرض سعر.",
        "ctaWa": "ابعت على واتساب",
        "faqKicker": "أسئلة شائعة",
        "relatedKicker": "خدمات أخرى",
        "relatedTitle": "ممكن كمان تحتاج",
        "processKicker": "خطوات التنفيذ",
        "factorsKicker": "إيه اللي بيحدد السعر؟",
        "worksKicker": "من أعمالنا",
        "updated": "آخر تحديث",
        "steps": [
            ("تواصل وفكرة", "ابعتلنا صور المكان أو فكرتك على واتساب ونتكلم عن المطلوب والميزانية."),
            ("معاينة ومقاسات", "فريقنا بيعاين ويرفع المقاسات بدقة ويرشحلك الخامة المناسبة."),
            ("تصميم وعرض سعر", "نتفق على الشكل والألوان والإكسسوارات وعرض سعر واضح بدون مفاجآت."),
            ("تصنيع في المصنع", "التصنيع بيتم في مصنعنا تحت إشرافنا المباشر وبمعايير جودة ثابتة."),
            ("تركيب وتسليم", "تركيب نظيف ومراجعة كل التفاصيل معاك قبل التسليم، مع ضمان ومتابعة."),
        ],
    },
    "en": {
        "brand": "El Gendy Genova Kitchens & Windows",
        "brandShort": "EL GENDY",
        "brandSub": "Genova · Kitchens & Windows",
        "city": "Mansoura",
        "workBy": "El Gendy Genova project, Mansoura",
        "home": "Home",
        "navServices": "Services",
        "navGuide": "Materials guide",
        "navWorks": "Our work",
        "navFaq": "FAQ",
        "navContact": "Contact",
        "mainMenu": "Main menu",
        "menu": "Menu",
        "darkMode": "Dark mode",
        "langLabel": "Language",
        "callNow": "Call now",
        "whatsapp": "WhatsApp",
        "waMessage": "Hello, I would like to ask about a service from El Gendy Genova",
        "freeConsult": "Book a free site visit",
        "seeWorks": "See our work",
        "learnMore": "See details →",
        "allPhotos": "Full project gallery →",
        "loadMore": "Show more",
        "moreOnFb": "All photos on Facebook",
        "all": "All",
        "close": "Close",
        "prev": "Previous",
        "next": "Next",
        "quoteTitle": "Request a visit or quote",
        "quoteLead": "Fill in the details and a ready WhatsApp message will open, straight to our team.",
        "quoteIntro": "Hello El Gendy Genova, I would like a site visit / quote",
        "fName": "Name", "fNamePh": "Your name",
        "fPhone": "Mobile number",
        "fService": "Work type",
        "fArea": "Area", "fAreaPh": "e.g. Mansoura – University district",
        "fMsg": "Details", "fMsgPh": "Approximate sizes, colors, or any idea you have",
        "fMore": "More than one service",
        "send": "Send via WhatsApp",
        "showroom": "Showroom",
        "showroomAddr": "Mansoura — end of Samia El-Gamal St., El-Sallab St.",
        "factory": "Factory",
        "factoryAddr": "Mansoura — behind the Central Security camp",
        "reach": "Talk to us",
        "openMap": "Open in Maps →",
        "chatWa": "Start a WhatsApp chat →",
        "footerAbout": "Aluminum and wood kitchens, UPVC and aluminum windows and doors, tempered glass and feature walls — built in our own factory and installed across Mansoura.",
        "footerServices": "Services",
        "footerLinks": "Links",
        "footerContact": "Contact",
        "footerCity": "Mansoura, Dakahlia, Egypt",
        "tagline": "Designed to Impress. Built to Last.",
        "ctaTitle": "No matter how small the space, we use every centimeter",
        "ctaLead": "Send a photo of the space and rough measurements, and we will get back to you with an initial concept and quote.",
        "ctaWa": "Send on WhatsApp",
        "faqKicker": "FAQ",
        "relatedKicker": "Other services",
        "relatedTitle": "You might also need",
        "processKicker": "How it works",
        "factorsKicker": "What sets the price?",
        "worksKicker": "Our work",
        "updated": "Last updated",
        "steps": [
            ("Idea & contact", "Send us photos of the space or your idea on WhatsApp and we discuss needs and budget."),
            ("Site visit", "Our team visits, takes precise measurements and recommends the right material."),
            ("Design & quote", "We agree on look, colors and accessories with a clear quote — no surprises."),
            ("Factory build", "Manufactured in our own factory under direct supervision and consistent quality checks."),
            ("Install & handover", "Clean installation and a full walk-through before handover, with warranty and follow-up."),
        ],
    },
}

# ---------------------------------------------------------------- Services
SERVICES = [
    {
        "slug": "aluminum-kitchens",
        "hero": 226,
        "cats": ["alukitchen"],
        "ar": {
            "name": "مطابخ ألوميتال",
            "card": "قطاعات ألوميتال قوية ضد الرطوبة والتسوس، بألوان وحشوات متنوعة وإكسسوارات عملية.",
            "title": "مطابخ ألوميتال في المنصورة | تصنيع وتركيب — الجندي جينوفا",
            "desc": "تصنيع وتركيب مطابخ ألوميتال في المنصورة بقطاعات قوية ضد المياه والتسوس، حشوات متنوعة وإكسسوارات عملية. معاينة ورفع مقاسات وعرض سعر واضح من الجندي جينوفا.",
            "h1": "مطابخ ألوميتال في المنصورة",
            "lead": "مطبخ يستحمل المية والبخار والاستخدام اليومي الشاق من غير ما يتنفخ أو يسوّس — بقطاعات ألوميتال قوية، وحشوات وألوان تختارها بنفسك، وتصنيع كامل في مصنعنا بالمنصورة.",
            "facts": ["ضد المياه والتسوس", "عمر افتراضي طويل", "حشوات وألوان متعددة", "تصنيع في مصنعنا"],
            "introTitle": "ليه مطبخ الألوميتال؟",
            "intro": [
                "مطابخ الألوميتال هي الاختيار العملي لكل بيت المطبخ فيه بيتعرّض لرطوبة عالية أو مية كتير: الحوض، الغسالة، والبخار اليومي. الألوميتال لا يتأثر بالمياه ولا يسوّس، فالمطبخ بيفضل محافظ على شكله واستقامته لسنين.",
                "بنصنّع الهيكل والضلف من قطاعات ألوميتال بسُمك مناسب للاستخدام، ونركّب عليها حشوات بالشكل اللي يعجبك: كلادينج، أكريليك، زجاج، أو خشب مقاوم للرطوبة، بألوان سادة أو خشبية أو لامعة.",
            ],
            "typesTitle": "اختيارات مطابخ الألوميتال",
            "types": [
                ("ضلف ألوميتال بحشو كلادينج", "خفيفة وسهلة التنظيف، وألوانها كتير جدًا من السادة للخشبي."),
                ("حشو أكريليك أو هاي جلوس", "لمعة وشكل عصري مع متانة الألوميتال من جوه."),
                ("ضلف زجاج بإطار ألوميتال", "للخزائن العلوية والفاترينات، مع إمكانية إضاءة LED."),
                ("أسطح رخام أو جرانيت", "نركّب السطح المناسب لاستخدامك ونقفل الحواف بشكل نظيف."),
                ("إكسسوارات مطبخ", "مجاري أدراج، مفصلات، صفايات، وأرفف داخلية حسب احتياجك."),
                ("مطابخ الشقق الإيجار والمصايف", "حل اقتصادي ومتين للأماكن اللي محتاجة مطبخ يتحمل من غير صيانة."),
            ],
            "whyTitle": "إمتى يكون الألوميتال هو الأنسب؟",
            "why": [
                "لو المطبخ صغير أو قليل التهوية والبخار بيتجمع فيه.",
                "لو الحوض أو الغسالة جنب الخزائن مباشرة.",
                "لو عايز مطبخ يعيش سنين طويلة بأقل صيانة.",
                "لو الميزانية محتاجة توازن بين السعر والمتانة.",
            ],
            "factors": [
                ("سُمك ونوع القطاع", "القطاعات الأتقل بتدي متانة أعلى وبتفرق في السعر."),
                ("نوع الحشو", "كلادينج، أكريليك، زجاج، أو خشب — كل خامة ليها سعر وشكل."),
                ("المقاسات وعدد الوحدات", "طول المطبخ وعدد الخزائن العلوية والسفلية."),
                ("الإكسسوارات", "المجاري والمفصلات والصفايات والأرفف الداخلية."),
                ("السطح", "رخام أو جرانيت ونوعه وسُمكه."),
            ],
            "faqs": [
                ("هل مطابخ الألوميتال بتصدّى أو بتتأثر بالمية؟", "لا، الألوميتال لا يصدأ ولا يتأثر بالمياه أو البخار، وده أهم سبب بيخلي الناس تختاره للمطبخ. بنختار حشوات مقاومة للرطوبة كمان عشان المطبخ كله يفضل سليم."),
                ("هل ينفع مطبخ الألوميتال يبقى شكله مودرن؟", "أكيد. مع حشوات الأكريليك أو الهاي جلوس أو الألوان الخشبية الحديثة، والمقابض المخفية، بيطلع مطبخ الألوميتال بشكل عصري جدًا."),
                ("مطبخ الألوميتال ولا الخشب أحسن؟", "الألوميتال أقوى في مقاومة المياه والتسوس، والخشب (MDF/HPL/أكريليك) أغنى في التشطيبات والشكل. ممكن كمان نعمل دمج بين الاتنين. في المعاينة بنرشحلك الأنسب لمكانك."),
                ("بتاخدوا وقت قد إيه في التنفيذ؟", "المدة بتختلف حسب حجم المطبخ والحشوات المختارة. بعد المعاينة والاتفاق على التصميم بنحدد جدول تصنيع وتركيب واضح ونلتزم بيه."),
            ],
        },
        "en": {
            "name": "Aluminum Kitchens",
            "card": "Strong aluminum profiles that resist moisture and termites, in many colors, infill panels and practical accessories.",
            "title": "Aluminum Kitchens in Mansoura | Made & Installed — El Gendy Genova",
            "desc": "Aluminum kitchens made and installed in Mansoura, Egypt: water- and termite-proof profiles, many infill panels and colors, practical fittings. Free site visit and clear quote from El Gendy Genova.",
            "h1": "Aluminum Kitchens in Mansoura",
            "lead": "A kitchen that handles water, steam and heavy daily use without swelling or rotting — strong aluminum profiles, infill panels and colors you choose, fully built in our Mansoura factory.",
            "facts": ["Water & termite-proof", "Long service life", "Many panels & colors", "Built in our factory"],
            "introTitle": "Why an aluminum kitchen?",
            "intro": [
                "Aluminum kitchens are the practical choice for homes where the kitchen sees a lot of moisture: the sink, the washing machine and daily cooking steam. Aluminum is not affected by water and cannot rot, so the kitchen keeps its shape and alignment for years.",
                "We build the carcass and doors from aluminum profiles sized for daily use, then fit the infill you like: cladding panels, acrylic, glass, or moisture-resistant board, in plain, wood-look or high-gloss colors.",
            ],
            "typesTitle": "Aluminum kitchen options",
            "types": [
                ("Aluminum doors with cladding infill", "Light, easy to clean, and available in a huge range of plain and wood-look colors."),
                ("Acrylic or high-gloss infill", "A glossy, modern look with aluminum strength underneath."),
                ("Glass doors in aluminum frames", "For wall cabinets and display units, with optional LED lighting."),
                ("Marble or granite worktops", "We fit the right top for your use and finish the edges cleanly."),
                ("Kitchen fittings", "Drawer runners, hinges, dish racks and inner shelves to suit your needs."),
                ("Rental flats & holiday homes", "An economical, durable kitchen that needs almost no maintenance."),
            ],
            "whyTitle": "When is aluminum the right choice?",
            "why": [
                "Small or poorly ventilated kitchens where steam builds up.",
                "When the sink or washing machine sits right next to the cabinets.",
                "When you want a kitchen that lasts for many years with minimal upkeep.",
                "When the budget needs a balance between price and durability.",
            ],
            "factors": [
                ("Profile gauge & type", "Heavier profiles give more strength and change the price."),
                ("Infill material", "Cladding, acrylic, glass or board — each has its own cost and look."),
                ("Size & number of units", "Kitchen run length and the count of wall and base cabinets."),
                ("Fittings", "Runners, hinges, dish racks and inner shelving."),
                ("Worktop", "Marble or granite, its type and thickness."),
            ],
            "faqs": [
                ("Do aluminum kitchens rust or get damaged by water?", "No. Aluminum does not rust and is not affected by water or steam — the main reason people choose it for kitchens. We also use moisture-resistant infill so the whole kitchen stays sound."),
                ("Can an aluminum kitchen look modern?", "Yes. With acrylic or high-gloss infill, modern wood-look colors and handle-less details, aluminum kitchens look very contemporary."),
                ("Aluminum or wood kitchen — which is better?", "Aluminum is stronger against water and rot; wood (MDF/HPL/acrylic) offers richer finishes. We can also combine both. At the site visit we recommend what suits your space."),
                ("How long does it take?", "It depends on kitchen size and the chosen infill. After the visit and design approval we give you a clear manufacturing and installation schedule and stick to it."),
            ],
        },
    },
    {
        "slug": "wood-kitchens",
        "hero": 22,
        "cats": ["modern", "classic", "details"],
        "ar": {
            "name": "مطابخ خشب",
            "card": "MDF و HPL وأكريليك وبولي لاك — تصميمات مودرن وكلاسيك بتقسيم داخلي ذكي لكل سنتيمتر.",
            "title": "مطابخ خشب مودرن وكلاسيك في المنصورة | MDF وأكريليك وHPL — الجندي جينوفا",
            "desc": "تصميم وتصنيع مطابخ خشب في المنصورة: مودرن وكلاسيك، MDF و HPL وأكريليك وبولي لاك، هاي جلوس أو مطفي، مع أركان دوّارة وأدراج ذكية وتركيب احترافي.",
            "h1": "مطابخ خشب مودرن وكلاسيك في المنصورة",
            "lead": "مهما كان ذوقك أو ستايلك… إحنا هننفّذ. مطابخ MDF و HPL وأكريليك وبولي لاك، بتقسيم داخلي يستغل كل سنتيمتر، وتشطيب هاي جلوس أو مطفي يليق ببيتك.",
            "facts": ["هاي جلوس أو مطفي", "مفصلات ومجاري هيدروليك", "أركان دوّارة وأدراج ذكية", "إضاءة LED"],
            "introTitle": "مطبخ معمول على مقاس بيتك",
            "intro": [
                "المطبخ مش مجرد مكان… ده جزء من تفاصيل بيتك. عشان كده بنبدأ بالمعاينة ورفع المقاسات، وبعدين نصمم توزيع يناسب طريقة استخدامك: مكان الثلاجة والبوتاجاز والحوض، وعدد الأدراج، والخزائن العلوية لحد السقف لو محتاج تخزين أكتر.",
                "بننفّذ الستايل المودرن بالخطوط النظيفة والمقابض المخفية والخزائن الزجاج المضاءة، والستايل الكلاسيك بالضلف المحفورة والألوان الخشبية الدافية — وكله بإكسسوارات عملية تريحك في الاستخدام اليومي.",
            ],
            "typesTitle": "الخامات والتشطيبات",
            "types": [
                ("MDF مدهون (بولي لاك)", "ألوان بلا حدود وتشطيب ناعم مطفي أو لامع."),
                ("أكريليك هاي جلوس", "لمعة مراية وشكل فخم، مثالي للمطابخ المودرن."),
                ("HPL", "سطح قوي ضد الخدوش والحرارة، مناسب للاستخدام الشاق."),
                ("خشب كلاسيك بضلف محفورة", "للي بيحبوا الطابع الدافي والتفاصيل الكلاسيكية."),
                ("خزائن زجاج بإضاءة LED", "فاترينات علوية تعرض الأطباق وتدي إضاءة جميلة للمطبخ."),
                ("أسطح رخام وجرانيت", "اختيارات ألوان وسُمك تناسب الستايل والاستخدام."),
            ],
            "whyTitle": "تفاصيل بتفرق في الاستخدام اليومي",
            "why": [
                "أركان دوّارة (كاروسيل) تستغل الزوايا الميتة.",
                "أدراج داخلية ومنظمات للمعالق والأدوات.",
                "مفصلات ومجاري هيدروليك تقفل بهدوء.",
                "صفايات أطباق مخفية وأماكن للأجهزة المدمجة.",
            ],
            "factors": [
                ("نوع الخامة", "MDF، HPL، أكريليك، أو بولي لاك — والفرق بينهم كبير في السعر والشكل."),
                ("التشطيب", "هاي جلوس أو مطفي، لون سادة أو خشبي."),
                ("المقاسات وارتفاع الخزائن", "خزائن لحد السقف بتزود التخزين والتكلفة."),
                ("الإكسسوارات", "الكاروسيل والأدراج الداخلية والمفصلات الهيدروليك."),
                ("السطح والأجهزة المدمجة", "نوع الرخام أو الجرانيت وتجهيزات الفرن والبوتاجاز المدمج."),
            ],
            "faqs": [
                ("إيه الفرق بين MDF و HPL والأكريليك؟", "الـ MDF المدهون بيدي ألوان بلا حدود وتشطيب ناعم، والـ HPL أقوى ضد الخدوش والحرارة، والأكريليك بيدي لمعة مراية وشكل فخم. بنوريك عينات حقيقية في المعرض قبل ما تختار."),
                ("هل ينفع أنفّذ مطبخ من صورة شفتها على النت؟", "أكيد. ابعت الصورة على واتساب ونطابقها مع مقاسات مكانك ونقترح الخامات والألوان الأقرب لها."),
                ("المطبخ الخشب بيتأثر بالمية؟", "بنستخدم ألواح مقاومة للرطوبة في وحدات الحوض والأماكن المعرضة للمية، ونقفل الحواف كويس. ولو المطبخ رطوبته عالية جدًا ممكن نرشحلك دمج مع الألوميتال."),
                ("هل بتركبوا الأجهزة المدمجة؟", "بنجهّز أماكن الفرن والبوتاجاز والغسالة وغسالة الأطباق المدمجة بالمقاسات المظبوطة، ونساعدك في التركيب والتوصيل."),
            ],
        },
        "en": {
            "name": "Wood Kitchens",
            "card": "MDF, HPL, acrylic and poly-lac, modern or classic, with smart interior layouts that use every centimeter.",
            "title": "Modern & Classic Wood Kitchens in Mansoura | MDF, Acrylic, HPL — El Gendy Genova",
            "desc": "Custom wood kitchens in Mansoura, Egypt: modern and classic designs in MDF, HPL, acrylic and poly-lac, high-gloss or matte, with corner carousels, smart drawers and professional installation.",
            "h1": "Modern & Classic Wood Kitchens in Mansoura",
            "lead": "Whatever your taste or style, we build it. MDF, HPL, acrylic and poly-lac kitchens with interior layouts that use every centimeter, finished in high-gloss or matte.",
            "facts": ["High-gloss or matte", "Soft-close hinges & runners", "Corner carousels & smart drawers", "LED lighting"],
            "introTitle": "A kitchen made to your home's measurements",
            "intro": [
                "A kitchen is not just a room — it is part of your home's character. We start with a site visit and precise measurements, then design a layout around how you cook: fridge, hob and sink positions, number of drawers, and ceiling-height wall units when you need more storage.",
                "We build modern kitchens with clean lines, handle-less doors and lit glass cabinets, and classic kitchens with carved doors and warm wood tones — always with practical fittings that make daily use easier.",
            ],
            "typesTitle": "Materials & finishes",
            "types": [
                ("Painted MDF (poly-lac)", "Unlimited colors with a smooth matte or gloss finish."),
                ("High-gloss acrylic", "A mirror-like shine and premium look, ideal for modern kitchens."),
                ("HPL", "A tough surface that resists scratches and heat for heavy use."),
                ("Classic carved wood doors", "For those who love warm tones and classic detailing."),
                ("Glass cabinets with LED", "Lit display wall units that show off dishes and light the room."),
                ("Marble & granite tops", "Colors and thicknesses to match the style and use."),
            ],
            "whyTitle": "Details that matter every day",
            "why": [
                "Corner carousels that use dead corner space.",
                "Inner drawers and cutlery organizers.",
                "Soft-close hinges and runners.",
                "Hidden dish racks and housings for built-in appliances.",
            ],
            "factors": [
                ("Material", "MDF, HPL, acrylic or poly-lac — big differences in price and look."),
                ("Finish", "High-gloss or matte, plain or wood-look."),
                ("Size & cabinet height", "Ceiling-height units add storage and cost."),
                ("Fittings", "Carousels, inner drawers and soft-close hardware."),
                ("Worktop & built-ins", "Marble or granite type and built-in oven/hob housings."),
            ],
            "faqs": [
                ("What is the difference between MDF, HPL and acrylic?", "Painted MDF gives unlimited colors and a smooth finish, HPL is tougher against scratches and heat, and acrylic offers a mirror shine and premium look. We show you real samples at the showroom before you choose."),
                ("Can you build a kitchen from a photo I found online?", "Absolutely. Send the photo on WhatsApp and we will adapt it to your measurements and suggest the closest materials and colors."),
                ("Are wood kitchens affected by water?", "We use moisture-resistant boards in sink units and wet areas and seal the edges well. For very humid kitchens we may suggest combining wood with aluminum."),
                ("Do you fit built-in appliances?", "We prepare exact housings for built-in ovens, hobs, washing machines and dishwashers and help with fitting and connection."),
            ],
        },
    },
    {
        "slug": "upvc-windows-doors",
        "hero": 97,
        "cats": ["upvc", "doors"],
        "ar": {
            "name": "شبابيك وأبواب UPVC",
            "card": "عزل للحرارة والصوت والأتربة، مفصلي أو جرار أو قلاب، وأبواب حمامات ومداخل بموديلات مختلفة.",
            "title": "شبابيك وأبواب UPVC في المنصورة | عزل حرارة وصوت — الجندي جينوفا",
            "desc": "تصنيع وتركيب شبابيك وأبواب UPVC في المنصورة: عزل حراري وصوتي، لا تصدأ، زجاج دبل، مفصلي وجرار وقلاب، أبواب حمامات ومداخل. معاينة مجانية وعرض سعر من الجندي جينوفا.",
            "h1": "شبابيك وأبواب UPVC في المنصورة",
            "lead": "اقفل على الحر والدوشة والتراب. شبابيك وأبواب UPVC معزولة، لا تصدأ ولا تحتاج صيانة، بأشكال مفصلي وجرار وقلاب وموديلات مقوّسة — من تصنيعنا وتركيبنا.",
            "facts": ["عزل حراري وصوتي", "لا يصدأ", "زجاج دبل اختياري", "أبيض أو ألوان خشبية"],
            "introTitle": "ليه UPVC؟",
            "intro": [
                "الـ UPVC خامة بلاستيكية مقوّاة بقلب معدني، بتتصنّع منها قطاعات فيها غرف هوا داخلية بتعزل الحرارة والصوت. مع جوانات محكمة وزجاج دبل، الشباك بيقفل كويس جدًا على الحر والبرد والدوشة والأتربة — وده بيفرق جدًا في الشقق المطلة على شوارع زحمة أو الأدوار العالية.",
                "القطاعات مش بتصدى ومش بتحتاج دهان، وتنضيفها بقطعة قماش. بنصنّع الشبابيك والأبواب بالمقاس، ونركّبها بتشطيب نظيف ومحكم حوالين الحلق.",
            ],
            "typesTitle": "أنواع الشبابيك والأبواب",
            "types": [
                ("شبابيك مفصلي (فتح للداخل)", "أعلى درجة إحكام وعزل، ومناسبة لغرف النوم والريسبشن."),
                ("شبابيك جرار", "توفر المساحة، ومناسبة للبلكونات والفتحات الكبيرة."),
                ("شبابيك قلاب (Tilt & Turn)", "تهوية آمنة من فوق مع إمكانية الفتح الكامل."),
                ("شبابيك مقوّسة وبتقسيمات", "قطاعات مقوّسة وتقسيمات ذهبي أو أبيض للواجهات الكلاسيك."),
                ("شبابيك مطابخ وحمامات بشفاط", "فتحة مجهزة لتركيب الشفاط مع زجاج مصنفر."),
                ("أبواب مداخل وحمامات", "موديلات بزجاج معشّق أو مصمتة، ضد المياه ولا تتأثر بالرطوبة."),
            ],
            "whyTitle": "مناسبة لمين؟",
            "why": [
                "الشقق المطلة على شوارع رئيسية أو قريبة من مصادر دوشة.",
                "الأدوار العالية المعرضة للهوا والتراب.",
                "الحمامات والمطابخ اللي محتاجة أبواب ضد المياه.",
                "اللي عايز يقلل استهلاك التكييف في الصيف.",
            ],
            "factors": [
                ("نوع القطاع وسُمكه", "عدد غرف العزل الداخلية ونوع الخامة."),
                ("نوع الزجاج", "سنجل أو دبل، شفاف أو مصنفر أو ملون."),
                ("طريقة الفتح", "مفصلي، جرار، أو قلاب."),
                ("المقاسات والتقسيمات", "الشبابيك المقوّسة والتقسيمات بتحتاج شغل أكتر."),
                ("الإكسسوارات واللون", "مقابض، كوالين، سلك، ولون أبيض أو خشبي."),
            ],
            "faqs": [
                ("هل شبابيك UPVC بتعزل الصوت فعلًا؟", "نعم، القطاعات فيها غرف هوا داخلية ومع الجوانات المحكمة والزجاج الدبل بتقلل الدوشة بشكل ملحوظ جدًا مقارنة بالشبابيك العادية."),
                ("هل الـ UPVC بيصفّر أو يتغير لونه مع الشمس؟", "القطاعات الجيدة معالجة ضد الأشعة فوق البنفسجية وبتحافظ على لونها. بنستخدم قطاعات من مصادر موثوقة وبنوريك العينات قبل التنفيذ."),
                ("ينفع أركّب UPVC مكان شبابيك قديمة؟", "أيوه، بنفك الشبابيك القديمة ونجهز الفتحة ونركّب الجديد بتشطيب نظيف حوالين الحلق."),
                ("UPVC ولا ألوميتال؟", "الـ UPVC أفضل في العزل والصوت، والألوميتال أفضل في المساحات الكبيرة والقطاعات النحيفة. اقرأ دليلنا الكامل للمقارنة أو اسألنا في المعاينة."),
            ],
        },
        "en": {
            "name": "UPVC Windows & Doors",
            "card": "Heat, noise and dust insulation in casement, sliding or tilt styles, plus bathroom and entrance doors.",
            "title": "UPVC Windows & Doors in Mansoura | Heat & Noise Insulation — El Gendy Genova",
            "desc": "UPVC windows and doors made and installed in Mansoura, Egypt: thermal and acoustic insulation, rust-free, double glazing, casement, sliding and tilt-and-turn, bathroom and entrance doors. Free site visit.",
            "h1": "UPVC Windows & Doors in Mansoura",
            "lead": "Shut out heat, noise and dust. Insulated UPVC windows and doors that never rust and need no maintenance — casement, sliding, tilt-and-turn and arched designs, made and installed by us.",
            "facts": ["Thermal & acoustic insulation", "Rust-free", "Optional double glazing", "White or wood-look"],
            "introTitle": "Why UPVC?",
            "intro": [
                "UPVC is a reinforced rigid PVC with a steel core, extruded into profiles with internal air chambers that insulate against heat and sound. With tight gaskets and double glazing, the window seals very well against heat, cold, noise and dust — a big difference for apartments on busy streets or on high floors.",
                "The profiles never rust, never need painting, and clean with a cloth. We make every window and door to measure and install it with a clean, sealed finish around the frame.",
            ],
            "typesTitle": "Window & door types",
            "types": [
                ("Casement windows (inward opening)", "The tightest seal and best insulation, ideal for bedrooms and living rooms."),
                ("Sliding windows", "Space-saving, great for balconies and wide openings."),
                ("Tilt & turn windows", "Safe top ventilation plus full opening when needed."),
                ("Arched & gridded windows", "Arched frames with gold or white grids for classic facades."),
                ("Kitchen & bathroom windows with fan", "A prepared opening for an exhaust fan with frosted glass."),
                ("Entrance & bathroom doors", "Decorative-glass or solid models, waterproof and humidity-proof."),
            ],
            "whyTitle": "Who is it for?",
            "why": [
                "Apartments facing main roads or other noise sources.",
                "High floors exposed to wind and dust.",
                "Bathrooms and kitchens that need waterproof doors.",
                "Anyone who wants to cut air-conditioning use in summer.",
            ],
            "factors": [
                ("Profile type & depth", "Number of internal chambers and material grade."),
                ("Glass type", "Single or double, clear, frosted or tinted."),
                ("Opening style", "Casement, sliding or tilt-and-turn."),
                ("Size & grids", "Arched shapes and grids require more work."),
                ("Hardware & color", "Handles, locks, insect screens, white or wood-look."),
            ],
            "faqs": [
                ("Do UPVC windows really reduce noise?", "Yes. The profiles have internal air chambers, and together with tight gaskets and double glazing they reduce noise very noticeably compared with ordinary windows."),
                ("Does UPVC turn yellow in the sun?", "Good profiles are UV-stabilized and keep their color. We use profiles from reliable sources and show you samples before production."),
                ("Can UPVC replace my old windows?", "Yes. We remove the old windows, prepare the opening and install the new ones with a clean finish around the frame."),
                ("UPVC or aluminum?", "UPVC insulates better against heat and noise; aluminum is better for large spans and slim frames. Read our full comparison guide or ask us at the site visit."),
            ],
        },
    },
    {
        "slug": "aluminum-windows-facades",
        "hero": 190,
        "cats": ["aluwindow"],
        "ar": {
            "name": "شبابيك وواجهات ألوميتال",
            "card": "شبابيك جرار ومفصلي، أبواب بلكونات، وواجهات محلات وزجاج بقطاعات نحيفة ومتينة.",
            "title": "شبابيك وواجهات ألوميتال في المنصورة | جرار ومفصلي وواجهات محلات — الجندي جينوفا",
            "desc": "تصنيع وتركيب شبابيك ألوميتال جرار ومفصلي، أبواب بلكونات، وواجهات محلات وزجاج في المنصورة. قطاعات نحيفة ومتينة وألوان إلكتروستاتيك متعددة من الجندي جينوفا.",
            "h1": "شبابيك وواجهات ألوميتال في المنصورة",
            "lead": "قطاعات نحيفة وقوية تسمح بمساحات زجاج أكبر وإضاءة طبيعية أكتر — شبابيك جرار ومفصلي، أبواب بلكونات، وواجهات محلات وفاترينات بتشطيب نظيف.",
            "facts": ["قطاعات نحيفة وقوية", "مساحات زجاج كبيرة", "ألوان إلكتروستاتيك", "واجهات محلات"],
            "introTitle": "الألوميتال للمساحات الكبيرة",
            "intro": [
                "الألوميتال معدن خفيف وقوي في نفس الوقت، فبيسمح بقطاعات نحيفة تشيل زجاج كبير من غير ما تتقوّس أو تتأثر بالحرارة. عشان كده هو الاختيار الأول للبلكونات والفتحات العريضة وواجهات المحلات.",
                "بنوفر ألوان إلكتروستاتيك كتير (أبيض، أسود، بني، رمادي، خشبي) وبنقفل التركيب بسيليكون وجوانات تمنع تسريب المية والهوا.",
            ],
            "typesTitle": "إيه اللي بننفذه بالألوميتال",
            "types": [
                ("شبابيك جرار", "ضلفتين أو تلاتة، بسلك أو من غير، للغرف والبلكونات."),
                ("شبابيك مفصلي", "فتح كامل وإحكام جيد للأماكن الصغيرة."),
                ("أبواب بلكونات", "أبواب جرار أو مفصلي بزجاج كبير ومقابض مريحة."),
                ("واجهات محلات وفاترينات", "واجهات زجاج كبيرة بأبواب دخول، لعرض أفضل لنشاطك."),
                ("شبابيك منحنية وبتقسيمات", "للفتحات الدائرية والمقوّسة والواجهات المميزة."),
                ("قواطيع زجاج", "فواصل داخلية للمكاتب والمساحات المفتوحة."),
            ],
            "whyTitle": "إمتى نختار الألوميتال؟",
            "why": [
                "الفتحات العريضة والبلكونات اللي محتاجة زجاج كبير.",
                "واجهات المحلات والمعارض والمكاتب.",
                "لو عايز إطار نحيف وشكل عصري بسيط.",
                "لو بتدور على توازن ممتاز بين السعر والمتانة.",
            ],
            "factors": [
                ("نوع وسُمك القطاع", "قطاعات تقيلة للمساحات الكبيرة والواجهات."),
                ("الزجاج", "سُمك الزجاج ونوعه: شفاف، فاميه، سيكوريت، أو دبل."),
                ("اللون", "ألوان الإلكتروستاتيك والخشبي."),
                ("المقاسات وطريقة الفتح", "جرار أو مفصلي وعدد الضلف."),
                ("الإكسسوارات", "كوالين، مقابض، عجل، وسلك."),
            ],
            "faqs": [
                ("هل الألوميتال بيعزل زي الـ UPVC؟", "الـ UPVC أعلى في العزل الحراري والصوتي، لكن الألوميتال مع جوانات كويسة وزجاج دبل بيدي عزل جيد جدًا، وبيتفوق في المساحات الكبيرة والقطاعات النحيفة."),
                ("بتعملوا واجهات محلات؟", "أيوه، بننفذ واجهات زجاج بالألوميتال للمحلات والمعارض بأبواب دخول وقطاعات تتحمل الأحجام الكبيرة."),
                ("إيه الألوان المتاحة؟", "أبيض، أسود، بني، رمادي، شامبين، وألوان خشبية — بنوريك كتالوج الألوان في المعرض."),
                ("الشبابيك الجرار بتسرّب مية في الشتا؟", "بنركّب قطاعات بمجرى تصريف وجوانات وفرش، وبنقفل حوالين الحلق بسيليكون عشان نمنع التسريب."),
            ],
        },
        "en": {
            "name": "Aluminum Windows & Facades",
            "card": "Sliding and hinged windows, balcony doors, shopfronts and glazing with slim, durable profiles.",
            "title": "Aluminum Windows & Shopfronts in Mansoura | Sliding, Hinged, Facades — El Gendy Genova",
            "desc": "Aluminum sliding and hinged windows, balcony doors, shopfronts and glazing made and installed in Mansoura, Egypt. Slim, strong profiles in many powder-coat colors from El Gendy Genova.",
            "h1": "Aluminum Windows & Facades in Mansoura",
            "lead": "Slim yet strong profiles that allow bigger glass and more daylight — sliding and hinged windows, balcony doors, and shopfronts with a clean finish.",
            "facts": ["Slim, strong profiles", "Large glass areas", "Powder-coat colors", "Shopfronts"],
            "introTitle": "Aluminum for large openings",
            "intro": [
                "Aluminum is light and strong at the same time, so slim profiles can carry large glass without bending or reacting to heat. That makes it the first choice for balconies, wide openings and shopfronts.",
                "We offer many powder-coat colors (white, black, brown, grey, wood-look) and seal every installation with silicone and gaskets to stop water and air leaks.",
            ],
            "typesTitle": "What we build in aluminum",
            "types": [
                ("Sliding windows", "Two or three sashes, with or without insect screens."),
                ("Hinged windows", "Full opening and a good seal for smaller spaces."),
                ("Balcony doors", "Sliding or hinged doors with large glass and comfortable handles."),
                ("Shopfronts & display windows", "Large glazed facades with entrance doors for better visibility."),
                ("Curved & gridded windows", "For round and arched openings and standout facades."),
                ("Glass partitions", "Interior dividers for offices and open spaces."),
            ],
            "whyTitle": "When to choose aluminum",
            "why": [
                "Wide openings and balconies that need large glass.",
                "Shop, showroom and office facades.",
                "When you want a slim frame and a clean modern look.",
                "When you want an excellent balance of price and durability.",
            ],
            "factors": [
                ("Profile type & gauge", "Heavier profiles for large spans and facades."),
                ("Glass", "Thickness and type: clear, tinted, tempered or double."),
                ("Color", "Powder-coat and wood-look finishes."),
                ("Size & opening", "Sliding or hinged and number of sashes."),
                ("Hardware", "Locks, handles, rollers and insect screens."),
            ],
            "faqs": [
                ("Does aluminum insulate as well as UPVC?", "UPVC insulates better against heat and noise, but aluminum with good gaskets and double glazing performs very well, and it excels in large spans and slim frames."),
                ("Do you build shopfronts?", "Yes. We build aluminum-and-glass facades for shops and showrooms with entrance doors and profiles rated for large sizes."),
                ("What colors are available?", "White, black, brown, grey, champagne and wood-look finishes — see the color catalog at our showroom."),
                ("Do sliding windows leak in winter?", "We install profiles with drainage channels, gaskets and brush seals, and seal around the frame with silicone to prevent leaks."),
            ],
        },
    },
    {
        "slug": "glass-showers",
        "hero": None,
        "cats": [],
        "ar": {
            "name": "زجاج سيكوريت للشاور",
            "card": "كبائن شاور من زجاج سيكوريت مقسّى، شفاف أو مصنفر، بإكسسوارات ستانلس مقاومة للصدأ.",
            "title": "كبائن شاور زجاج سيكوريت في المنصورة | تفصيل وتركيب — الجندي جينوفا",
            "desc": "تفصيل وتركيب كبائن شاور زجاج سيكوريت مقسّى في المنصورة: مفصلي وجرار وثابت، شفاف أو مصنفر، بإكسسوارات ستانلس ستيل. معاينة ورفع مقاسات من الجندي جينوفا.",
            "h1": "كبائن شاور زجاج سيكوريت في المنصورة",
            "lead": "حمام أنظف وأشيك بكابينة زجاج سيكوريت مقسّى متفصّلة على مقاس المكان — شفاف أو مصنفر، مفصلي أو جرار، بإكسسوارات ستانلس ما بتصداش.",
            "facts": ["زجاج مقسّى آمن", "تفصيل على المقاس", "إكسسوارات ستانلس", "شفاف أو مصنفر"],
            "introTitle": "ليه زجاج سيكوريت؟",
            "intro": [
                "زجاج السيكوريت (المقسّى) بيتعالج حراريًا عشان يبقى أقوى بكتير من الزجاج العادي، ولو اتكسر — لا قدر الله — بيتفتت لحبيبات صغيرة مش حادة. ده بيخليه الخامة الآمنة الوحيدة المناسبة لكبائن الشاور.",
                "بنرفع المقاسات بدقة لأن الحيطان والأرضيات نادرًا ما تكون مظبوطة 100%، وبنفصّل الزجاج والإكسسوارات على المقاس الفعلي عشان الكابينة تقفل كويس من غير تسريب.",
            ],
            "typesTitle": "أشكال كبائن الشاور",
            "types": [
                ("باب مفصلي", "باب زجاج بيفتح على مفصلات ستانلس، مع جزء ثابت حسب المساحة."),
                ("جرار (سلايدنج)", "مثالي للحمامات الضيقة لأنه مش محتاج مساحة فتح."),
                ("زاوية (كورنر)", "كابينة ركنية بضلعين تستغل زاوية الحمام."),
                ("حاجز ثابت (ووك إن)", "لوح زجاج ثابت بشكل مودرن ومفتوح."),
                ("مصنفر أو بتصميم", "خصوصية أكتر مع شكل أنيق."),
                ("إكسسوارات ستانلس", "مفصلات ومقابض وجوانات مقاومة للمية والصدأ."),
            ],
            "whyTitle": "مميزات الكابينة الزجاج",
            "why": [
                "بتحافظ على باقي الحمام ناشف ونضيف.",
                "شكل أوسع وأشيك من الستارة.",
                "تنظيف سهل وعمر طويل.",
                "آمنة بفضل الزجاج المقسّى.",
            ],
            "factors": [
                ("سُمك الزجاج", "الأسماك الأكبر أمتن وأتقل."),
                ("نوع الزجاج", "شفاف، مصنفر، أو بتصميم."),
                ("شكل الكابينة", "مفصلي، جرار، كورنر، أو ثابت."),
                ("المقاسات", "عرض وارتفاع المساحة."),
                ("الإكسسوارات", "نوع ولون المفصلات والمقابض والمجاري."),
            ],
            "faqs": [
                ("زجاج السيكوريت آمن في الحمام؟", "نعم، ده الزجاج الآمن المستخدم في كبائن الشاور لأنه أقوى بكتير من العادي، ولو اتكسر بيتفتت لحبيبات صغيرة غير حادة."),
                ("الحمام صغير، ينفع أعمل كابينة؟", "أيوه، الكابينة الجرار أو الحاجز الثابت مناسبين جدًا للحمامات الصغيرة لأنهم مش محتاجين مساحة فتح."),
                ("الكابينة بتسرّب مية؟", "بنفصّل على المقاس الفعلي ونركّب جوانات مخصوص للشاور ونظبط الميول، عشان المية تفضل جوه الكابينة."),
                ("ممكن أشوف شغل سابق؟", "أكيد، ابعتلنا على واتساب وهنبعتلك صور كبائن نفّذناها، أو زورنا في المعرض."),
            ],
        },
        "en": {
            "name": "Tempered Glass Showers",
            "card": "Shower enclosures in tempered security glass, clear or frosted, with rust-resistant stainless fittings.",
            "title": "Tempered Glass Shower Enclosures in Mansoura | Made to Measure — El Gendy Genova",
            "desc": "Made-to-measure tempered (securit) glass shower enclosures in Mansoura, Egypt: hinged, sliding, corner and fixed walk-in panels, clear or frosted, with stainless steel fittings. Site visit and measurements included.",
            "h1": "Tempered Glass Shower Enclosures in Mansoura",
            "lead": "A cleaner, more elegant bathroom with a tempered glass shower enclosure cut to your exact space — clear or frosted, hinged or sliding, with stainless fittings that never rust.",
            "facts": ["Safe tempered glass", "Made to measure", "Stainless fittings", "Clear or frosted"],
            "introTitle": "Why tempered (securit) glass?",
            "intro": [
                "Tempered glass is heat-treated to be several times stronger than ordinary glass, and if it ever breaks it crumbles into small, blunt pieces. That makes it the only safe choice for shower enclosures.",
                "We measure precisely because walls and floors are rarely perfectly square, then cut the glass and fittings to the real dimensions so the enclosure closes well without leaks.",
            ],
            "typesTitle": "Enclosure styles",
            "types": [
                ("Hinged door", "A glass door on stainless hinges, with a fixed panel where needed."),
                ("Sliding", "Ideal for narrow bathrooms because it needs no swing space."),
                ("Corner", "A two-sided corner enclosure that uses the bathroom corner."),
                ("Fixed walk-in panel", "A single fixed glass panel for an open, modern look."),
                ("Frosted or patterned", "More privacy with an elegant finish."),
                ("Stainless fittings", "Hinges, handles and seals resistant to water and rust."),
            ],
            "whyTitle": "Benefits of a glass enclosure",
            "why": [
                "Keeps the rest of the bathroom dry and clean.",
                "Looks more spacious and elegant than a curtain.",
                "Easy to clean and long-lasting.",
                "Safe thanks to tempered glass.",
            ],
            "factors": [
                ("Glass thickness", "Thicker glass is sturdier and heavier."),
                ("Glass type", "Clear, frosted or patterned."),
                ("Enclosure style", "Hinged, sliding, corner or fixed."),
                ("Dimensions", "Width and height of the space."),
                ("Fittings", "Type and finish of hinges, handles and tracks."),
            ],
            "faqs": [
                ("Is tempered glass safe in a bathroom?", "Yes. It is the safety glass used in shower enclosures because it is much stronger than ordinary glass and breaks into small, blunt pieces."),
                ("My bathroom is small — can I still have an enclosure?", "Yes. Sliding enclosures and fixed walk-in panels suit small bathrooms because they need no swing space."),
                ("Will it leak?", "We cut to the real measurements, fit shower-specific seals and check floor falls so water stays inside the enclosure."),
                ("Can I see previous work?", "Of course — message us on WhatsApp and we will send photos of enclosures we have installed, or visit our showroom."),
            ],
        },
    },
    {
        "slug": "wall-decor-tv-units",
        "hero": 0,
        "cats": ["decor"],
        "ar": {
            "name": "ديكورات حوائط وشاشات",
            "card": "وحدات تلفزيون وخلفيات حوائط بإضاءة مخفية ورفوف، تكمّل ستايل الريسبشن أو الصالة.",
            "title": "ديكورات حوائط ووحدات شاشات في المنصورة | TV Unit بإضاءة مخفية — الجندي جينوفا",
            "desc": "تصميم وتنفيذ ديكورات حوائط ووحدات شاشات تلفزيون في المنصورة: خلفيات بإضاءة LED مخفية، رفوف ووحدات تخزين، تكسيات حجر وخشب. من الجندي جينوفا.",
            "h1": "ديكورات حوائط ووحدات شاشات في المنصورة",
            "lead": "حائط الشاشة هو أول حاجة بتلفت النظر في الريسبشن. بنصمم وننفّذ وحدات تلفزيون وخلفيات حوائط بإضاءة مخفية ورفوف، تكمّل ستايل البيت وتخفي الأسلاك.",
            "facts": ["إضاءة LED مخفية", "إخفاء الأسلاك", "رفوف ووحدات تخزين", "تكسيات حجر وخشب"],
            "introTitle": "حائط يغيّر شكل المكان",
            "intro": [
                "وحدة الشاشة المتصممة صح بتنظم المكان: مكان للرسيفر والراوتر، أدراج للتخزين، رفوف للديكور، وإضاءة مخفية بتدي عمق ودفء للحائط — ومن غير ولا سلك ظاهر.",
                "بننفّذ خلفيات بخامات مختلفة زي الخشب والـ MDF المدهون والتكسيات الحجرية والشرائح (البانوهات)، وبنظبطها مع ألوان الأثاث والأرضيات.",
            ],
            "typesTitle": "إيه اللي بننفّذه",
            "types": [
                ("وحدة شاشة معلقة", "شكل خفيف ونظيف مع إضاءة سفلية."),
                ("حائط شاشة كامل", "خلفية من الأرض للسقف برفوف ووحدات جانبية."),
                ("إضاءة LED مخفية", "بروفايلات إضاءة دافية أو بيضاء حوالين الشاشة والرفوف."),
                ("تكسيات حجر وشرائح", "خلفيات حجرية أو شرائح خشب لعمق وملمس."),
                ("رفوف ومكتبات", "للديكور والكتب بتوزيع متوازن."),
                ("كاونترات وبارات", "بار مطبخ مفتوح بتكسية حجر زي اللي في أعمالنا."),
            ],
            "whyTitle": "ليه تعمل وحدة شاشة متفصّلة؟",
            "why": [
                "مقاسها مظبوط على الحائط والشاشة.",
                "تخفي كل الأسلاك والأجهزة.",
                "تخزين إضافي من غير ما تزحم المكان.",
                "بتتنفذ بنفس ستايل وألوان باقي البيت.",
            ],
            "factors": [
                ("مساحة الحائط", "عرض وارتفاع الحائط المطلوب تغطيته."),
                ("الخامات", "خشب، MDF مدهون، تكسية حجر، أو شرائح."),
                ("الإضاءة", "طول بروفايلات الـ LED ونوعها."),
                ("وحدات التخزين", "عدد الأدراج والضلف والرفوف."),
                ("التشطيب", "مطفي أو لامع ولون خشبي أو سادة."),
            ],
            "faqs": [
                ("هل بتخفوا أسلاك الشاشة؟", "نعم، بنعمل مسارات مخفية للأسلاك ومكان للرسيفر والراوتر جوه الوحدة."),
                ("ينفع أختار لون الإضاءة؟", "أيوه، إضاءة دافية أو بيضاء أو حتى قابلة للتحكم، حسب الجو اللي عايزه."),
                ("بتنفذوا ديكورات غير حائط الشاشة؟", "بننفذ خلفيات حوائط وبارات وكاونترات بتكسيات حجر وخشب، ابعتلنا فكرتك ونشوفها مع بعض."),
                ("ممكن أشوف تصميم قبل التنفيذ؟", "بنتفق معاك على الشكل والمقاسات والخامات بالتفصيل قبل التصنيع، ومعاها عرض سعر واضح."),
            ],
        },
        "en": {
            "name": "Feature Walls & TV Units",
            "card": "TV units and wall cladding with hidden lighting and shelving to complete your living room style.",
            "title": "Feature Walls & TV Units in Mansoura | Hidden LED Lighting — El Gendy Genova",
            "desc": "Custom TV units and feature walls in Mansoura, Egypt: hidden LED lighting, shelving and storage, stone and wood cladding, hidden cables. Designed and built by El Gendy Genova.",
            "h1": "Feature Walls & TV Units in Mansoura",
            "lead": "The TV wall is the first thing people notice in a living room. We design and build TV units and feature walls with hidden lighting and shelving that match your home and hide every cable.",
            "facts": ["Hidden LED lighting", "Cable management", "Shelves & storage", "Stone & wood cladding"],
            "introTitle": "A wall that changes the room",
            "intro": [
                "A well-designed TV unit organizes the room: space for the receiver and router, drawers for storage, shelves for decor, and hidden lighting that gives the wall depth and warmth — with no visible cables.",
                "We build feature walls in wood, painted MDF, stone cladding and slatted panels, matched to your furniture and flooring.",
            ],
            "typesTitle": "What we build",
            "types": [
                ("Floating TV unit", "A light, clean look with under-lighting."),
                ("Full TV wall", "Floor-to-ceiling backdrop with shelving and side units."),
                ("Hidden LED lighting", "Warm or cool light profiles around the screen and shelves."),
                ("Stone & slatted cladding", "Stone or wood-slat backdrops for depth and texture."),
                ("Shelving & bookcases", "Balanced layouts for decor and books."),
                ("Counters & bars", "Open-kitchen bars with stone cladding, as in our projects."),
            ],
            "whyTitle": "Why a custom TV unit?",
            "why": [
                "Sized exactly to your wall and screen.",
                "Hides all cables and devices.",
                "Extra storage without cluttering the room.",
                "Built in the same style and colors as the rest of your home.",
            ],
            "factors": [
                ("Wall area", "Width and height to be covered."),
                ("Materials", "Wood, painted MDF, stone cladding or slats."),
                ("Lighting", "Length and type of LED profiles."),
                ("Storage units", "Number of drawers, doors and shelves."),
                ("Finish", "Matte or gloss, wood-look or plain."),
            ],
            "faqs": [
                ("Do you hide the TV cables?", "Yes. We build hidden cable routes and a space for the receiver and router inside the unit."),
                ("Can I choose the light color?", "Yes — warm, cool, or even dimmable lighting, depending on the mood you want."),
                ("Do you build other decor besides TV walls?", "We build wall backdrops, bars and counters in stone and wood cladding. Send us your idea and we will work it out together."),
                ("Can I see the design before production?", "We agree on the look, sizes and materials in detail before manufacturing, with a clear quote."),
            ],
        },
    },
]

# ---------------------------------------------------------------- Home
HOME = {
    "ar": {
        "title": "الجندي جينوفا للمطابخ والشبابيك | مطابخ وشبابيك ألوميتال و UPVC في المنصورة",
        "desc": "الجندي جينوفا للمطابخ والشبابيك في المنصورة: تصنيع وتركيب مطابخ ألوميتال وخشب، شبابيك وأبواب ألوميتال و UPVC، زجاج سيكوريت للشاور، وديكورات حوائط ووحدات شاشات من مصنعنا.",
        "heroTitle": "الجندي جينوفا",
        "heroSub": "للمطابخ والشبابيك",
        "heroLead": "من مصنعنا في المنصورة إلى بيتك: نصمم ونصنّع ونركّب مطابخ عصرية، شبابيك وأبواب عازلة، زجاج سيكوريت للشاور، وديكورات حوائط وشاشات بتشطيب يليق ببيتك ويعيش معاك سنين.",
        "mosaic": ["مطبخ هاي جلوس بخزائن زجاج", "مطبخ مودرن", "شباك UPVC مقوّس"],
        "stats": [("مصنع خاص", "تصنيع داخل مصنعنا بالمنصورة"), ("+160", "صورة من أعمال منفّذة فعليًا"), ("6 خدمات", "مطابخ، شبابيك، أبواب، زجاج، ديكور"), ("ضمان حقيقي", "على التصنيع والتركيب")],
        "servicesKicker": "خدماتنا",
        "servicesTitle": "كل اللي بيتك محتاجه… من مكان واحد",
        "servicesLead": "بدل ما تتعامل مع أكثر من ورشة، بننفّذ المطبخ والشبابيك والأبواب والزجاج والديكور بنفس الذوق ونفس مستوى التشطيب، وبفريق تركيب واحد مسؤول عن النتيجة.",
        "matKicker": "دليل الخامات",
        "matTitle": "ألوميتال ولا UPVC ولا خشب؟",
        "matLead": "كل خامة ليها مكانها الصح. اعرف الفرق بسرعة، وعند المعاينة بنرشحلك الأنسب لمكانك وميزانيتك.",
        "matGuide": "اقرأ المقارنة الكاملة: ألوميتال ولا UPVC؟ ←",
        "bestFor": "الأنسب لـ:",
        "materials": [
            ("upvc", "UPVC", 73, "UPVC — العزل أولًا", "الاختيار المثالي للشقق المطلة على شوارع زحمة أو الأدوار العالية، لأنه بيقفل على الحر والدوشة والتراب.",
             ["عزل حراري وصوتي عالي", "لا يصدأ ولا يتأثر بالرطوبة", "إمكانية زجاج دبل", "صيانة شبه معدومة", "أبيض أو ألوان خشبية", "مفصلي، جرار، قلاب"],
             "غرف النوم، الريسبشن، المطابخ والحمامات بشفاط."),
            ("alu", "ألوميتال", 190, "ألوميتال — قوة ومساحات زجاج أكبر", "قطاعات نحيفة وقوية تسمح بفتحات وزجاج أكبر، ومناسبة للواجهات والبلكونات والمطابخ اللي محتاجة تتحمل رطوبة.",
             ["قطاعات نحيفة وشكل عصري", "يتحمل المساحات الكبيرة", "ألوان إلكتروستاتيك متعددة", "مطابخ ضد المياه والتسوس", "واجهات محلات وفاترينات", "تكلفة مناسبة"],
             "البلكونات، الواجهات، المحلات، ومطابخ الاستخدام الشاق."),
            ("wood", "خشب", 22, "خشب — الدفا والشياكة", "MDF و HPL وأكريليك وبولي لاك بتشطيبات مطفية أو هاي جلوس، لمطبخ شكله فخم ومريح في الاستخدام اليومي.",
             ["تشكيلة ألوان وتشطيبات ضخمة", "هاي جلوس أو مطفي", "مفصلات ومجاري هيدروليك", "أركان دوّارة وأدراج ذكية", "خزائن زجاج بإضاءة LED", "رخام أو جرانيت حسب الذوق"],
             "المطابخ المفتوحة، البيوت الجديدة، ومحبي الستايل المودرن."),
        ],
        "worksTitle": "شغل حقيقي… من بيوت عملائنا",
        "worksLead": "كل الصور دي لمشاريع نفّذناها بإيدينا في المنصورة. اضغط على أي صورة لعرضها بالحجم الكامل، أو افتح المعرض الكامل.",
        "processTitle": "من أول مكالمة لحد التسليم",
        "processLead": "خطوات واضحة ومواعيد محددة، ومتابعة منّا في كل مرحلة عشان تستلم شغلك زي ما اتفقنا بالظبط.",
        "reelsKicker": "فيديوهات",
        "reelsTitle": "شوف الشغل وهو بيتركّب",
        "reelsLead": "ريلز قصيرة من المصنع ومن مواقع التركيب على صفحتنا في فيسبوك — تفاصيل التشطيب أوضح بالفيديو.",
        "reels": [(24, "مطبخ بخزائن زجاج", "إضاءة LED وتشطيب هاي جلوس"), (14, "استغلال كل سنتيمتر", "أركان دوّارة وأدراج داخلية"), (93, "تركيب شبابيك UPVC", "قطاعات مقوّسة بتقسيمات ذهبي"), (165, "أبواب مداخل UPVC", "موديلات بزجاج معشّق")],
        "whyKicker": "ليه الجندي؟",
        "whyTitle": "اختيارك الأول للجودة والثقة",
        "whyItems": [("factory", "مصنع مش وسيط", "بنصنّع بنفسنا في مصنعنا، فبنتحكم في الجودة والمواعيد والسعر."), ("shield", "ضمان حقيقي", "ضمان مكتوب على التصنيع والتركيب، ومتابعة بعد التسليم."), ("grid", "تصميم عصري بمقاساتك", "كل قطعة بتتفصّل على مكانك، مش مقاسات جاهزة."), ("clock", "التزام بالمواعيد", "جدول تنفيذ واضح من البداية، وتواصل مباشر معانا طول الوقت.")],
        "visitKicker": "زورنا",
        "visitTitle": "المعرض والمصنع في المنصورة",
        "visitLead": "تعالى شوف الخامات والقطاعات والألوان على الطبيعة قبل ما تقرر، أو كلّمنا ونيجي لحد عندك.",
        "faqTitle": "قبل ما تطلب… إجابات سريعة",
        "faqLead": "لو سؤالك مش موجود، ابعته على واتساب وهنرد عليك بسرعة.",
        "faqs": [
            ("هل تقومون بالمعاينة ورفع المقاسات؟", "نعم، نحدد موعد معاينة لرفع المقاسات الدقيقة ومراجعة المكان قبل التصنيع، ويمكنك البدء بإرسال صور ومقاسات تقريبية على واتساب."),
            ("ما الفرق بين شبابيك الألوميتال و UPVC؟", "الـ UPVC يتميز بعزل أعلى للحرارة والصوت ولا يصدأ، بينما الألوميتال يتميز بقطاعات نحيفة وقوية ومساحات زجاج كبيرة. نساعدك على الاختيار حسب المكان والميزانية."),
            ("كم يستغرق تنفيذ المطبخ أو الشبابيك؟", "تختلف المدة حسب حجم الشغل ونوع الخامة. بعد المعاينة والاتفاق على التصميم نحدد لك جدول تصنيع وتركيب واضح ونلتزم به."),
            ("هل يوجد ضمان؟", "نعم، نقدم ضمانًا حقيقيًا على التصنيع والتركيب حسب نوع المنتج، مع متابعة بعد التسليم."),
            ("هل تعملون خارج المنصورة؟", "مقرنا في المنصورة ونخدم محافظة الدقهلية والمناطق القريبة. تواصل معنا وحدد موقعك وهنأكد لك إمكانية التنفيذ."),
            ("هل يمكن تنفيذ تصميم من صورة شفتها؟", "أكيد. ابعت الصورة على واتساب ونطابقها مع مقاسات مكانك ونقترح الخامات والألوان الأقرب لها."),
        ],
    },
    "en": {
        "title": "El Gendy Genova | Kitchens, Aluminum & UPVC Windows in Mansoura, Egypt",
        "desc": "El Gendy Genova Kitchens & Windows, Mansoura: we manufacture and install aluminum and wood kitchens, aluminum and UPVC windows and doors, tempered glass showers, and TV wall units in our own factory.",
        "heroTitle": "El Gendy Genova",
        "heroSub": "Premium Kitchens & Windows",
        "heroLead": "From our own factory in Mansoura to your home: we design, build and install modern kitchens, insulated windows and doors, tempered glass showers, and feature walls finished to last for years.",
        "mosaic": ["High-gloss kitchen with glass cabinets", "Modern kitchen", "Arched UPVC window"],
        "stats": [("Own factory", "Everything built in-house in Mansoura"), ("160+", "Photos of real completed projects"), ("6 services", "Kitchens, windows, doors, glass, decor"), ("Real warranty", "On manufacturing and installation")],
        "servicesKicker": "Services",
        "servicesTitle": "Everything your home needs, from one place",
        "servicesLead": "Instead of juggling several workshops, we deliver your kitchen, windows, doors, glass and decor with one style, one finishing standard, and one installation team accountable for the result.",
        "matKicker": "Materials guide",
        "matTitle": "Aluminum, UPVC or wood?",
        "matLead": "Each material has its right place. Here is the quick difference — at the site visit we recommend what suits your space and budget.",
        "matGuide": "Read the full comparison: aluminum or UPVC? →",
        "bestFor": "Best for:",
        "materials": [
            ("upvc", "UPVC", 73, "UPVC — insulation first", "The ideal choice for apartments on busy streets or high floors, because it shuts out heat, noise and dust.",
             ["High thermal & acoustic insulation", "Never rusts, moisture-proof", "Double glazing available", "Almost zero maintenance", "White or wood-look colors", "Casement, sliding, tilt"],
             "Bedrooms, living rooms, kitchens and bathrooms with exhaust fans."),
            ("alu", "Aluminum", 190, "Aluminum — strength and bigger glass", "Slim yet strong profiles allow larger openings and more glass — great for facades, balconies, and kitchens that must handle moisture.",
             ["Slim profiles, modern look", "Handles large spans", "Many powder-coat colors", "Water & termite-proof kitchens", "Shopfronts & display windows", "Cost-effective"],
             "Balconies, facades, shops and heavy-use kitchens."),
            ("wood", "Wood", 22, "Wood — warmth and elegance", "MDF, HPL, acrylic and poly-lac in matte or high-gloss finishes for a kitchen that looks premium and works hard every day.",
             ["Huge range of colors & finishes", "High-gloss or matte", "Soft-close hinges & runners", "Corner carousels & smart drawers", "Glass cabinets with LED", "Marble or granite tops"],
             "Open kitchens, new homes and modern-style lovers."),
        ],
        "worksTitle": "Real projects, from our clients’ homes",
        "worksLead": "Every photo here is a project we built and installed in Mansoura. Tap any photo to view it full size, or open the full gallery.",
        "processTitle": "From the first call to handover",
        "processLead": "Clear steps, fixed dates, and follow-up at every stage so you receive exactly what we agreed on.",
        "reelsKicker": "Videos",
        "reelsTitle": "Watch the work being installed",
        "reelsLead": "Short reels from the factory and installation sites on our Facebook page — finishing details look clearer on video.",
        "reels": [(24, "Glass-cabinet kitchen", "LED lighting & high-gloss finish"), (14, "Every centimeter used", "Corner carousels & inner drawers"), (93, "UPVC window install", "Arched frames with gold grids"), (165, "UPVC entrance doors", "Models with decorative glass")],
        "whyKicker": "Why El Gendy?",
        "whyTitle": "Your first choice for quality and trust",
        "whyItems": [("factory", "A factory, not a middleman", "We build everything ourselves, so we control quality, timing and price."), ("shield", "Real warranty", "Written warranty on manufacturing and installation, with after-sales follow-up."), ("grid", "Modern design, your sizes", "Every piece is tailored to your space — no off-the-shelf sizes."), ("clock", "On-time delivery", "A clear schedule from day one and direct contact throughout.")],
        "visitKicker": "Visit us",
        "visitTitle": "Showroom & factory in Mansoura",
        "visitLead": "Come see the materials, profiles and colors in person before you decide — or call us and we will come to you.",
        "faqTitle": "Quick answers before you order",
        "faqLead": "Can’t find your question? Send it on WhatsApp and we will reply quickly.",
        "faqs": [
            ("Do you do site visits and measurements?", "Yes. We schedule a visit to take precise measurements and review the space before manufacturing. You can start by sending photos and rough sizes on WhatsApp."),
            ("What is the difference between aluminum and UPVC windows?", "UPVC offers better heat and sound insulation and never rusts, while aluminum offers slim, strong profiles and larger glass areas. We help you choose based on location and budget."),
            ("How long does a kitchen or window project take?", "It depends on project size and material. After the visit and design approval we give you a clear manufacturing and installation schedule and stick to it."),
            ("Is there a warranty?", "Yes, we provide a real warranty on manufacturing and installation depending on the product, with follow-up after handover."),
            ("Do you work outside Mansoura?", "We are based in Mansoura and serve Dakahlia governorate and nearby areas. Share your location and we will confirm."),
            ("Can you build a design from a photo I saw?", "Absolutely. Send the photo on WhatsApp and we will adapt it to your measurements and suggest the closest materials and colors."),
        ],
    },
}

# ---------------------------------------------------------------- Gallery page
GALLERY = {
    "ar": {
        "title": "معرض أعمال الجندي جينوفا | صور مطابخ وشبابيك وأبواب منفّذة في المنصورة",
        "desc": "أكثر من 160 صورة حقيقية لمطابخ ألوميتال وخشب، شبابيك وأبواب UPVC وألوميتال، وواجهات وديكورات نفّذها الجندي جينوفا في المنصورة.",
        "h1": "معرض أعمالنا",
        "lead": "صور حقيقية من مشاريع نفّذناها بإيدينا — مطابخ، شبابيك، أبواب، واجهات وديكورات. اختار القسم اللي يهمك واضغط على أي صورة لعرضها بالحجم الكامل.",
    },
    "en": {
        "title": "El Gendy Genova Project Gallery | Kitchens, Windows & Doors in Mansoura",
        "desc": "160+ real photos of aluminum and wood kitchens, UPVC and aluminum windows and doors, facades and feature walls built by El Gendy Genova in Mansoura, Egypt.",
        "h1": "Our project gallery",
        "lead": "Real photos from projects we built ourselves — kitchens, windows, doors, facades and decor. Pick a category and tap any photo to view it full size.",
    },
}

# ---------------------------------------------------------------- Guide article
GUIDE = {
    "slug": "aluminum-vs-upvc",
    "hero": 73,
    "ar": {
        "title": "ألوميتال ولا UPVC؟ الفرق الكامل وأيهما أنسب لبيتك (دليل 2026) — الجندي جينوفا",
        "desc": "مقارنة عملية بين شبابيك الألوميتال و UPVC: العزل الحراري والصوتي، المتانة، الشكل، الصيانة، والعوامل اللي بتحدد السعر — ومتى تختار كل خامة. دليل من مصنع الجندي جينوفا بالمنصورة.",
        "h1": "ألوميتال ولا UPVC؟ الفرق الكامل وأيهما أنسب لبيتك",
        "lead": "سؤال بنسمعه كل يوم في المعرض. الإجابة المختصرة: الاتنين ممتازين، بس كل واحد ليه مكانه. الدليل ده بيشرحلك الفرق بوضوح عشان تختار صح.",
        "tldrTitle": "الخلاصة في سطرين",
        "tldr": "اختار UPVC لو أولويتك العزل من الحر والدوشة والتراب (غرف النوم، الشقق على شوارع رئيسية، الأدوار العالية). واختار الألوميتال لو محتاج فتحات وزجاج كبير بإطار نحيف (البلكونات، الواجهات، المحلات)، أو لو بتدور على أفضل توازن بين السعر والمتانة.",
        "toc": "المحتوى",
        "sections": [
            ("what", "يعني إيه ألوميتال ويعني إيه UPVC؟", """
<p><strong>الألوميتال</strong> هو قطاعات من سبائك الألومنيوم، خفيفة وقوية ولا تصدأ، وبتتدهن إلكتروستاتيك بألوان كتير. قوته بتسمح بإطارات نحيفة تشيل زجاج كبير.</p>
<p><strong>الـ UPVC</strong> هو بلاستيك PVC مقوّى (غير ملدّن) بيتصنّع منه قطاعات فيها <strong>غرف هوا داخلية</strong> وقلب معدني للتقوية. الغرف دي هي سر العزل العالي للحرارة والصوت.</p>
"""),
            ("compare", "مقارنة سريعة جنب بعض", """
<div class="table-wrap"><table>
<thead><tr><th>المعيار</th><th>UPVC</th><th>ألوميتال</th></tr></thead>
<tbody>
<tr><td>العزل الحراري</td><td>عالي جدًا بفضل الغرف الداخلية</td><td>جيد، ويتحسن مع الزجاج الدبل والجوانات</td></tr>
<tr><td>العزل الصوتي</td><td>ممتاز، الأفضل للشوارع الزحمة</td><td>متوسط إلى جيد</td></tr>
<tr><td>حجم الفتحات</td><td>مناسب للمقاسات العادية والمتوسطة</td><td>ممتاز للفتحات والواجهات الكبيرة</td></tr>
<tr><td>سُمك الإطار</td><td>أعرض نسبيًا</td><td>نحيف وعصري</td></tr>
<tr><td>الصدأ والرطوبة</td><td>لا يصدأ ولا يتأثر</td><td>لا يصدأ ولا يتأثر</td></tr>
<tr><td>الصيانة</td><td>شبه معدومة، تنضيف بقماشة</td><td>قليلة، ومراجعة الجوانات والعجل للجرار</td></tr>
<tr><td>الألوان</td><td>أبيض أو ألوان خشبية</td><td>ألوان إلكتروستاتيك كتير جدًا</td></tr>
<tr><td>الاستخدام الأشهر</td><td>غرف النوم والريسبشن والحمامات</td><td>البلكونات والواجهات والمحلات</td></tr>
</tbody></table></div>
"""),
            ("insulation", "العزل: الحر والدوشة والتراب", """
<p>لو الشقة على شارع رئيسي أو في دور عالي، العزل هو أهم معيار. قطاعات الـ UPVC فيها غرف هوا متعددة بتقطع انتقال الحرارة والصوت، ومع الجوانات المحكمة وطريقة الفتح المفصلي أو القلاب، الشباك بيقفل بإحكام شديد.</p>
<p>الألوميتال موصّل للحرارة بطبيعته، لكن مع <strong>زجاج دبل</strong> وجوانات وفرش جيدة بيوصل لعزل كويس جدًا، خصوصًا في الشبابيك المفصلي.</p>
<p>نصيحة من المعرض: الشبابيك الجرار — من أي خامة — عزلها أقل من المفصلي، لأن الضلف بتتحرك على مجرى. لو العزل أولويتك، اختار مفصلي أو قلاب.</p>
"""),
            ("size", "الشكل والمساحات الكبيرة", """
<p>هنا الألوميتال بيكسب. قوته بتسمح بقطاعات نحيفة تشيل ضلف زجاج عريضة من غير ما تتقوّس، وده بيدي إضاءة طبيعية أكتر وشكل أنظف — عشان كده هو الاختيار الطبيعي لـ <a href="{svc:aluminum-windows-facades}">الواجهات والبلكونات وواجهات المحلات</a>.</p>
<p>الـ UPVC بيدي شكل أنيق جدًا في المقاسات العادية، وبينفع في الأشكال المقوّسة والتقسيمات الكلاسيك زي اللي في <a href="{gallery}">معرض أعمالنا</a>.</p>
"""),
            ("price", "إيه اللي بيحدد السعر؟", """
<p>الأسعار بتتغير مع أسعار الخامات، فبدل رقم ثابت ممكن يبقى قديم، دي العوامل اللي فعلًا بتحدد تكلفة الشباك:</p>
<ul>
<li><strong>نوع القطاع وسُمكه</strong> — عدد الغرف في الـ UPVC، ووزن القطاع في الألوميتال.</li>
<li><strong>الزجاج</strong> — سنجل أو دبل، شفاف أو مصنفر أو سيكوريت.</li>
<li><strong>طريقة الفتح</strong> — مفصلي وقلاب أغلى غالبًا من الجرار.</li>
<li><strong>المقاس والشكل</strong> — المقوّس والتقسيمات بيحتاجوا شغل أكتر.</li>
<li><strong>الإكسسوارات</strong> — كوالين، مقابض، سلك، وماركة الهاردوير.</li>
</ul>
<p>عشان تاخد سعر دقيق لبيتك، <a href="{contact}">ابعتلنا المقاسات أو احجز معاينة</a> وبنحسبلك العرض بالتفصيل.</p>
"""),
            ("choose", "طيب أختار إيه؟", """
<h3>اختار UPVC لو:</h3>
<ul>
<li>الشقة على شارع زحمة أو جنب مصدر دوشة.</li>
<li>عايز تقلل الحر والتراب وتوفر في التكييف.</li>
<li>بتغيّر شبابيك غرف النوم والريسبشن أو أبواب الحمامات.</li>
</ul>
<h3>اختار الألوميتال لو:</h3>
<ul>
<li>عندك فتحات عريضة أو بلكونة محتاجة زجاج كبير.</li>
<li>بتعمل واجهة محل أو معرض أو مكتب.</li>
<li>عايز إطار نحيف بلون مميز، أو بتدور على أفضل سعر مقابل المتانة.</li>
</ul>
<p>وكتير من البيوت بتجمع الاتنين: <a href="{svc:upvc-windows-doors}">UPVC لغرف النوم</a> وألوميتال للبلكونات. ونفس المنطق ينطبق على المطابخ: <a href="{svc:aluminum-kitchens}">مطابخ الألوميتال</a> للأماكن الرطبة، و<a href="{svc:wood-kitchens}">المطابخ الخشب</a> لتشطيبات أغنى.</p>
"""),
        ],
        "faqs": [
            ("هل UPVC أحسن من الألوميتال؟", "مش أحسن بشكل مطلق. الـ UPVC أفضل في العزل الحراري والصوتي، والألوميتال أفضل في الفتحات الكبيرة والإطارات النحيفة والألوان. الاختيار حسب المكان واحتياجك."),
            ("أنهي أرخص: الألوميتال ولا UPVC؟", "السعر بيعتمد على نوع القطاع والزجاج وطريقة الفتح والمقاسات أكتر من الخامة نفسها. ابعتلنا المقاسات ونديك عرض سعر للخامتين عشان تقارن."),
            ("هل الـ UPVC بيستحمل حر الصيف في مصر؟", "نعم، القطاعات الجيدة معالجة ضد الأشعة فوق البنفسجية ومصممة تستحمل درجات الحرارة العالية من غير ما تتشوه أو يتغير لونها."),
            ("ينفع أجمع بين الألوميتال و UPVC في نفس الشقة؟", "أيوه وده شائع جدًا: UPVC لغرف النوم والريسبشن عشان العزل، وألوميتال للبلكونات والفتحات الكبيرة."),
        ],
    },
    "en": {
        "title": "Aluminum vs UPVC Windows: The Complete Comparison (2026 Guide) — El Gendy Genova",
        "desc": "A practical comparison of aluminum and UPVC windows: heat and noise insulation, strength, looks, maintenance and what drives the price — and when to choose each. A guide from El Gendy Genova's factory in Mansoura, Egypt.",
        "h1": "Aluminum vs UPVC: the complete comparison, and which suits your home",
        "lead": "We hear this question every day at our showroom. The short answer: both are excellent, but each has its place. This guide explains the difference clearly so you can choose with confidence.",
        "tldrTitle": "The answer in two lines",
        "tldr": "Choose UPVC if your priority is insulation against heat, noise and dust (bedrooms, flats on main roads, high floors). Choose aluminum if you need large openings and big glass in a slim frame (balconies, facades, shops), or the best balance of price and durability.",
        "toc": "Contents",
        "sections": [
            ("what", "What are aluminum and UPVC?", """
<p><strong>Aluminum</strong> windows are made from aluminum-alloy profiles: light, strong, rust-free, and powder-coated in many colors. Their strength allows slim frames that carry large glass.</p>
<p><strong>UPVC</strong> is unplasticized, rigid PVC extruded into profiles with <strong>internal air chambers</strong> and a steel reinforcing core. Those chambers are the secret behind its high heat and sound insulation.</p>
"""),
            ("compare", "Side-by-side comparison", """
<div class="table-wrap"><table>
<thead><tr><th>Criterion</th><th>UPVC</th><th>Aluminum</th></tr></thead>
<tbody>
<tr><td>Thermal insulation</td><td>Very high thanks to internal chambers</td><td>Good, improved with double glazing and gaskets</td></tr>
<tr><td>Sound insulation</td><td>Excellent — best for busy streets</td><td>Moderate to good</td></tr>
<tr><td>Opening size</td><td>Suited to standard and medium sizes</td><td>Excellent for large openings and facades</td></tr>
<tr><td>Frame width</td><td>Relatively wider</td><td>Slim and modern</td></tr>
<tr><td>Rust & humidity</td><td>Does not rust or react</td><td>Does not rust or react</td></tr>
<tr><td>Maintenance</td><td>Almost none — wipe with a cloth</td><td>Low; check gaskets and rollers on sliders</td></tr>
<tr><td>Colors</td><td>White or wood-look</td><td>A very wide powder-coat range</td></tr>
<tr><td>Typical use</td><td>Bedrooms, living rooms, bathrooms</td><td>Balconies, facades, shops</td></tr>
</tbody></table></div>
"""),
            ("insulation", "Insulation: heat, noise and dust", """
<p>If your flat faces a main road or sits on a high floor, insulation is the most important criterion. UPVC profiles have multiple air chambers that block heat and sound transfer, and with tight gaskets and casement or tilt-and-turn opening, the window seals very tightly.</p>
<p>Aluminum conducts heat by nature, but with <strong>double glazing</strong>, good gaskets and brush seals it reaches very good insulation, especially in hinged windows.</p>
<p>Showroom tip: sliding windows — in any material — insulate less than casement windows because the sashes run on a track. If insulation is your priority, choose casement or tilt-and-turn.</p>
"""),
            ("size", "Looks and large openings", """
<p>This is where aluminum wins. Its strength allows slim profiles to carry wide glass panels without bending, giving more daylight and a cleaner look — which is why it is the natural choice for <a href="{svc:aluminum-windows-facades}">facades, balconies and shopfronts</a>.</p>
<p>UPVC looks very elegant in standard sizes and works well for arched shapes and classic grids, as you can see in <a href="{gallery}">our gallery</a>.</p>
"""),
            ("price", "What drives the price?", """
<p>Prices move with material costs, so instead of a fixed number that quickly goes out of date, here are the factors that actually determine what a window costs:</p>
<ul>
<li><strong>Profile type and depth</strong> — number of chambers in UPVC, profile weight in aluminum.</li>
<li><strong>Glass</strong> — single or double, clear, frosted or tempered.</li>
<li><strong>Opening style</strong> — casement and tilt-and-turn usually cost more than sliding.</li>
<li><strong>Size and shape</strong> — arches and grids take more work.</li>
<li><strong>Hardware</strong> — locks, handles, insect screens and hardware brand.</li>
</ul>
<p>For an accurate price for your home, <a href="{contact}">send us your measurements or book a site visit</a> and we will prepare a detailed quote.</p>
"""),
            ("choose", "So which should I choose?", """
<h3>Choose UPVC if:</h3>
<ul>
<li>Your flat faces a busy road or another noise source.</li>
<li>You want less heat and dust and lower air-conditioning bills.</li>
<li>You are replacing bedroom and living-room windows or bathroom doors.</li>
</ul>
<h3>Choose aluminum if:</h3>
<ul>
<li>You have wide openings or a balcony that needs large glass.</li>
<li>You are building a shop, showroom or office front.</li>
<li>You want a slim frame in a distinctive color, or the best price-to-durability ratio.</li>
</ul>
<p>Many homes combine both: <a href="{svc:upvc-windows-doors}">UPVC for bedrooms</a> and aluminum for balconies. The same logic applies to kitchens: <a href="{svc:aluminum-kitchens}">aluminum kitchens</a> for humid spaces and <a href="{svc:wood-kitchens}">wood kitchens</a> for richer finishes.</p>
"""),
        ],
        "faqs": [
            ("Is UPVC better than aluminum?", "Not absolutely. UPVC is better for heat and sound insulation; aluminum is better for large openings, slim frames and colors. The right choice depends on the location and your needs."),
            ("Which is cheaper, aluminum or UPVC?", "Price depends more on the profile, glass, opening style and size than on the material itself. Send us your measurements and we will quote both so you can compare."),
            ("Can UPVC handle Egyptian summer heat?", "Yes. Quality profiles are UV-stabilized and designed for high temperatures without warping or changing color."),
            ("Can I combine aluminum and UPVC in the same flat?", "Yes, and it is very common: UPVC for bedrooms and living rooms for insulation, aluminum for balconies and large openings."),
        ],
    },
}
