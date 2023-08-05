from typing import Dict

from .. import Provider as LoremProvider


class Provider(LoremProvider):
    """Implement lorem provider for ``ar_AA`` locale."""

    word_list = (
        "أثره",
        "أجزاء",
        "أحدث",
        "أحكم",
        "أخذ",
        "أخر",
        "أخرى",
        "أدنى",
        "أدوات",
        "أراض",
        "أراضي",
        "أسابيع",
        "أساسي",
        "أسر",
        "أسيا",
        "أصقاع",
        "أضف",
        "أطراف",
        "أعلنت",
        "أعمال",
        "أفاق",
        "أفريقيا",
        "أكثر",
        "ألمانيا",
        "ألمّ",
        "أم",
        "أما",
        "أمام",
        "أمدها",
        "أملاً",
        "أمّا",
        "أن",
        "أهّل",
        "أواخر",
        "أوراقهم",
        "أوروبا",
        "أوزار",
        "أوسع",
        "أي",
        "إبّان",
        "إتفاقية",
        "إجلاء",
        "إحتار",
        "إحكام",
        "إختار",
        "إذ",
        "إستعمل",
        "إستيلاء",
        "إعادة",
        "إعلان",
        "إعمار",
        "إنطلاق",
        "إيطاليا",
        "إيو",
        "ابتدعها",
        "اتفاق",
        "اتفاقية",
        "اتّجة",
        "احداث",
        "ارتكبها",
        "اسبوعين",
        "استبدال",
        "استدعى",
        "استراليا",
        "استرجاع",
        "استطاعوا",
        "استعملت",
        "استمرار",
        "اعتداء",
        "اعلان",
        "اقتصادية",
        "اكتوبر",
        "الآخر",
        "الآلاف",
        "الأبرياء",
        "الأثناء",
        "الأثنان",
        "الأجل",
        "الأحمر",
        "الأخذ",
        "الأراضي",
        "الأرض",
        "الأرضية",
        "الأرواح",
        "الأسيوي",
        "الأعمال",
        "الأمريكي",
        "الأمريكية",
        "الأمم",
        "الأمور",
        "الأهداف",
        "الأوربيين",
        "الأوروبي",
        "الأوروبية",
        "الأوروبيّون",
        "الأوضاع",
        "الأول",
        "الأولى",
        "الإتحاد",
        "الإتفاقية",
        "الإثنان",
        "الإحتفاظ",
        "الإطلاق",
        "الإقتصادي",
        "الإقتصادية",
        "الإكتفاء",
        "الإمتعاض",
        "الإمداد",
        "الإنذار",
        "الإنزال",
        "الإيطالية",
        "الا",
        "الانجليزية",
        "الاندونيسية",
        "الباهضة",
        "البرية",
        "البشريةً",
        "البولندي",
        "التاريخ",
        "التبرعات",
        "التجارية",
        "التحالف",
        "التخطيط",
        "التغييرات",
        "التقليدي",
        "التقليدية",
        "التكاليف",
        "التنازلي",
        "التي",
        "الثالث",
        "الثانية",
        "الثقيل",
        "الثقيلة",
        "الجديدة",
        "الجنرال",
        "الجنوب",
        "الجنوبي",
        "الجنود",
        "الجو",
        "الجوي",
        "الحدود",
        "الحرة",
        "الحكم",
        "الحكومة",
        "الحيلولة",
        "الخارجية",
        "الخاسر",
        "الخاسرة",
        "الخاصّة",
        "الخاطفة",
        "الخطّة",
        "الدمج",
        "الدنمارك",
        "الدول",
        "الدولارات",
        "الدّفاع",
        "الذود",
        "الرئيسية",
        "الربيع",
        "الساحة",
        "الساحل",
        "الساحلية",
        "السادس",
        "السبب",
        "الستار",
        "السفن",
        "السيء",
        "السيطرة",
        "الشتاء",
        "الشتوية",
        "الشرق",
        "الشرقي",
        "الشرقية",
        "الشطر",
        "الشمال",
        "الشمل",
        "الشهير",
        "الشهيرة",
        "الشّعبين",
        "الصعداء",
        "الصفحات",
        "الصفحة",
        "الصين",
        "الصينية",
        "الضروري",
        "الضغوط",
        "الطرفين",
        "الطريق",
        "العاصمة",
        "العالم",
        "العالمي",
        "العالمية",
        "العدّ",
        "العصبة",
        "العظمى",
        "العمليات",
        "العناد",
        "الغالي",
        "الفترة",
        "الفرنسي",
        "الفرنسية",
        "القادة",
        "القوى",
        "الكونجرس",
        "اللا",
        "اللازمة",
        "الله",
        "المؤلّفة",
        "المارق",
        "المبرمة",
        "المتاخمة",
        "المتحدة",
        "المتساقطة",
        "المتّبعة",
        "المجتمع",
        "المحيط",
        "المدن",
        "المسرح",
        "المشترك",
        "المشتّتون",
        "المضي",
        "المعاهدات",
        "المنتصر",
        "المواد",
        "الموسوعة",
        "النزاع",
        "النفط",
        "الهادي",
        "الهجوم",
        "الواقعة",
        "الوراء",
        "الوزراء",
        "الولايات",
        "الى",
        "اليابان",
        "اليابانية",
        "اليميني",
        "اليها",
        "ان",
        "انتباه",
        "انتصارهم",
        "انتهت",
        "انذار",
        "انه",
        "اوروبا",
        "ايطاليا",
        "بأراضي",
        "بأسر",
        "بأضرار",
        "بأم",
        "بأيدي",
        "بإعمار",
        "باستحداث",
        "باستخدام",
        "بال",
        "بالأجل",
        "بالإنزال",
        "بالتوقيع",
        "بالثالث",
        "بالجانب",
        "بالجوي",
        "بالحرب",
        "بالرغم",
        "بالرّد",
        "بالرّغم",
        "بالسادس",
        "بالسيطرة",
        "بالشتاء",
        "بالشرقي",
        "بالعمل",
        "بالمحور",
        "بالمطالبة",
        "بالولايات",
        "بانه",
        "ببحشد",
        "ببعض",
        "ببلا",
        "ببه",
        "بتحت",
        "بتحدّي",
        "بتخصيص",
        "بتصفح",
        "بتطويق",
        "بتونس",
        "بجسيمة",
        "بحث",
        "بحشد",
        "بحق",
        "بحيث",
        "بخطوط",
        "بدارت",
        "بداية",
        "بدول",
        "بدون",
        "بريطانيا",
        "بريطانيا-فرنسا",
        "بزمام",
        "بسبب",
        "بشرية",
        "بشكل",
        "بضرب",
        "بعد",
        "بعدم",
        "بعرض",
        "بعشوائية",
        "بعض",
        "بعلى",
        "بـ",
        "بفرض",
        "بفصل",
        "بقادة",
        "بقد",
        "بقسوة",
        "بقصف",
        "بقعة",
        "بقيادة",
        "بكلا",
        "بكلّ",
        "بل",
        "بلا",
        "بلاده",
        "بلديهما",
        "بلمّ",
        "بلها",
        "بمباركة",
        "بمحاولة",
        "بمما",
        "بنقطة",
        "به",
        "بها",
        "بهناك",
        "بهيئة",
        "بوابة",
        "بوقامت",
        "بولاتّساع",
        "بولم",
        "بولندا",
        "بيكن",
        "بين",
        "بينما",
        "ب٠٨٠٤",
        "ب٣٠",
        "تاريخ",
        "تجهيز",
        "تحت",
        "تحرير",
        "تحرّك",
        "تحرّكت",
        "ترتيب",
        "تزامناً",
        "تسبب",
        "تسمّى",
        "تشكيل",
        "تشيكوسلوفاكيا",
        "تصرّف",
        "تصفح",
        "تطوير",
        "تعد",
        "تعداد",
        "تعديل",
        "تغييرات",
        "تكاليف",
        "تكبّد",
        "تكتيكاً",
        "تلك",
        "تم",
        "تمهيد",
        "تنفّس",
        "تونس",
        "تُصب",
        "ثانية",
        "ثم",
        "ثمّة",
        "جدول",
        "جديداً",
        "جديدة",
        "جزيرتي",
        "جسيمة",
        "جعل",
        "جمعت",
        "جنوب",
        "جهة",
        "جورج",
        "جيما",
        "جيوب",
        "جُل",
        "حادثة",
        "حالية",
        "حاملات",
        "حاول",
        "حتى",
        "حدى",
        "حصدت",
        "حقول",
        "حكومة",
        "حلّت",
        "حول",
        "حيث",
        "حين",
        "خطّة",
        "خلاف",
        "خيار",
        "دأبوا",
        "دار",
        "دارت",
        "دخول",
        "دفّة",
        "دنو",
        "دول",
        "دون",
        "ديسمبر",
        "ذات",
        "ذلك",
        "رئيس",
        "رجوعهم",
        "زهاء",
        "سابق",
        "ساعة",
        "سبتمبر",
        "سقطت",
        "سقوط",
        "سكان",
        "سليمان",
        "سنغافورة",
        "سياسة",
        "شاسعة",
        "شدّت",
        "شرسة",
        "شعار",
        "شمال",
        "شموليةً",
        "شواطيء",
        "شيء",
        "صفحة",
        "ضرب",
        "ضمنها",
        "طوكيو",
        "عالمية",
        "عجّل",
        "عدد",
        "عدم",
        "عرض",
        "عرفها",
        "عسكرياً",
        "عشوائية",
        "عقبت",
        "عل",
        "علاقة",
        "على",
        "عليها",
        "عملية",
        "عن",
        "عُقر",
        "غريمه",
        "غرّة",
        "غضون",
        "غير",
        "غينيا",
        "فاتّبع",
        "فبعد",
        "فرنسا",
        "فرنسية",
        "فسقط",
        "فشكّل",
        "فصل",
        "فعل",
        "فقامت",
        "فقد",
        "فكان",
        "فكانت",
        "فمرّ",
        "فهرست",
        "في",
        "قائمة",
        "قادة",
        "قام",
        "قامت",
        "قبضتهم",
        "قبل",
        "قتيل",
        "قد",
        "قدما",
        "قررت",
        "قُدُماً",
        "قِبل",
        "كان",
        "كانت",
        "كانتا",
        "كثيرة",
        "كردة",
        "كرسي",
        "كل",
        "كلا",
        "كلّ",
        "كما",
        "كنقطة",
        "كُلفة",
        "لأداء",
        "لإعادة",
        "لإعلان",
        "لإنعدام",
        "لان",
        "لبلجيكا",
        "لبولندا",
        "لتقليعة",
        "لدحر",
        "لعدم",
        "لعملة",
        "لغات",
        "لفرنسا",
        "لفشل",
        "لكل",
        "لكون",
        "للأراضي",
        "للإتحاد",
        "للجزر",
        "للحكومة",
        "للسيطرة",
        "للصين",
        "للمجهود",
        "لليابان",
        "لم",
        "لمحاكم",
        "لمّ",
        "لها",
        "لهذه",
        "لهيمنة",
        "ليبين",
        "ليتسنّى",
        "ليرتفع",
        "ليركز",
        "مئات",
        "ما",
        "ماذا",
        "مارد",
        "ماشاء",
        "ماليزيا",
        "مايو",
        "محاولات",
        "مدن",
        "مدينة",
        "مرجع",
        "مرمى",
        "مسؤولية",
        "مسارح",
        "مساعدة",
        "مسرح",
        "مشارف",
        "مشاركة",
        "مشروط",
        "مع",
        "معارضة",
        "معاملة",
        "معزّزة",
        "معقل",
        "مقاطعة",
        "مقاومة",
        "مكثّفة",
        "مكن",
        "مكّن",
        "مليارات",
        "مليون",
        "مما",
        "ممثّلة",
        "من",
        "منتصف",
        "مهمّات",
        "مواقعها",
        "موالية",
        "ميناء",
        "نتيجة",
        "نفس",
        "نقطة",
        "نهاية",
        "هاربر",
        "هامش",
        "هذا",
        "هذه",
        "هنا؟",
        "هناك",
        "هو",
        "هُزم",
        "و",
        "وأزيز",
        "وأكثرها",
        "وإعلان",
        "وإقامة",
        "وإيطالي",
        "واتّجه",
        "واحدة",
        "واستمر",
        "واستمرت",
        "واشتدّت",
        "واعتلاء",
        "واقتصار",
        "والإتحاد",
        "والتي",
        "والحزب",
        "والديون",
        "والروسية",
        "والعتاد",
        "والفرنسي",
        "والفلبين",
        "والقرى",
        "والكساد",
        "والكوري",
        "والمانيا",
        "والمعدات",
        "والنرويج",
        "والنفيس",
        "وانتهاءً",
        "واندونيسيا",
        "وانهاء",
        "وايرلندا",
        "واُسدل",
        "وباءت",
        "وباستثناء",
        "وبالتحديد",
        "وبالرغم",
        "وبحلول",
        "وبدأت",
        "وبداية",
        "وبدون",
        "وبريطانيا",
        "وبعد",
        "وبعدما",
        "وبعض",
        "وبغطاء",
        "وبلجيكا",
        "وبولندا",
        "وتتحمّل",
        "وترك",
        "وتزويده",
        "وتم",
        "وتنامت",
        "وتنصيب",
        "وجزر",
        "وجهان",
        "وحتى",
        "وحتّى",
        "وحرمان",
        "وحلفاؤها",
        "ودول",
        "وزارة",
        "وسفن",
        "وسمّيت",
        "وسوء",
        "وشعار",
        "وصافرات",
        "وصغار",
        "وصل",
        "وعلى",
        "وعُرفت",
        "وفرنسا",
        "وفنلندا",
        "وفي",
        "وقام",
        "وقبل",
        "وقد",
        "وقدّموا",
        "وقرى",
        "وقوعها",
        "وكسبت",
        "ولاتّساع",
        "ولكسمبورغ",
        "ولم",
        "ومحاولة",
        "ومضى",
        "ومطالبة",
        "ومن",
        "ونتج",
        "وهولندا",
        "ووصف",
        "ويتّفق",
        "ويعزى",
        "ويكيبيديا",
        "يبق",
        "يتبقّ",
        "يتسنّى",
        "يتعلّق",
        "يتم",
        "يتمكن",
        "يذكر",
        "يرتبط",
        "يطول",
        "يعادل",
        "يعبأ",
        "يقوم",
        "يكن",
        "يونيو",
        "٠٨٠٤",
        "٢٠٠٤",
        "٣٠",
    )

    parts_of_speech: Dict[str, tuple] = {}
