from typing import Dict

from .. import Provider as LoremProvider


class Provider(LoremProvider):
    """Implement lorem provider for ``cs_CZ`` locale.

    Word list is drawn from the SYN2015.
    (representative corpus of contemporary written Czech published in December 2015)

    The word list is a list of the 2000 most common lemmas. Abbreviations and first names were removed.

    Sources:
    - https://wiki.korpus.cz/lib/exe/fetch.php/seznamy:syn2015_lemma_utf8.zip

    """

    word_list = (
        "a",
        "aby",
        "adresa",
        "Afrika",
        "agentura",
        "akce",
        "aktivita",
        "aktivní",
        "aktuální",
        "ale",
        "alespoň",
        "alkohol",
        "americký",
        "Amerika",
        "analýza",
        "anebo",
        "anglický",
        "ani",
        "aniž",
        "ano",
        "aplikace",
        "architekt",
        "areál",
        "armáda",
        "asi",
        "aspoň",
        "atmosféra",
        "auto",
        "autobus",
        "autor",
        "avšak",
        "ačkoli",
        "ať",
        "až",
        "babička",
        "banka",
        "barevný",
        "barva",
        "bavit",
        "bez",
        "bezpečnost",
        "bezpečnostní",
        "bezpečný",
        "blok",
        "blízko",
        "blízký",
        "blížit",
        "bod",
        "bohatý",
        "bohužel",
        "boj",
        "bojovat",
        "bok",
        "bolest",
        "bota",
        "boží",
        "branka",
        "bratr",
        "britský",
        "Brno",
        "brněnský",
        "brzy",
        "brána",
        "bránit",
        "brát",
        "budoucnost",
        "budoucí",
        "budova",
        "buď",
        "buňka",
        "bydlet",
        "byt",
        "byť",
        "bát",
        "bílý",
        "být",
        "bývalý",
        "bývat",
        "během",
        "běžet",
        "běžný",
        "břeh",
        "březen",
        "břicho",
        "bůh",
        "celek",
        "celkem",
        "celkový",
        "celý",
        "cena",
        "centrum",
        "cesta",
        "charakter",
        "chladný",
        "chlap",
        "chlapec",
        "chodba",
        "chodit",
        "chovat",
        "chování",
        "chránit",
        "chtít",
        "chuť",
        "chvilka",
        "chvíle",
        "chyba",
        "chybět",
        "chystat",
        "chytit",
        "chápat",
        "cigareta",
        "cizí",
        "co",
        "cokoli",
        "cosi",
        "což",
        "cukr",
        "cíl",
        "církev",
        "cítit",
        "daleko",
        "další",
        "daný",
        "datum",
        "daň",
        "dařit",
        "dcera",
        "dech",
        "den",
        "denně",
        "deník",
        "deset",
        "design",
        "deska",
        "desítka",
        "detail",
        "devět",
        "diskuse",
        "displej",
        "dispozice",
        "divadlo",
        "divoký",
        "divák",
        "dlaň",
        "dle",
        "dlouho",
        "dlouhodobý",
        "dlouhý",
        "dnes",
        "dneska",
        "dnešní",
        "dno",
        "do",
        "doba",
        "dobrý",
        "dobře",
        "docela",
        "docházet",
        "dodat",
        "dodnes",
        "dodávat",
        "dohoda",
        "dohromady",
        "dojem",
        "dojít",
        "dokonalý",
        "dokonce",
        "dokončit",
        "doktor",
        "dokud",
        "dokument",
        "dokázat",
        "dolar",
        "dolů",
        "doma",
        "domnívat",
        "domov",
        "domácnost",
        "domácí",
        "domů",
        "dopadnout",
        "dopis",
        "doplnit",
        "doporučovat",
        "doprava",
        "dopravní",
        "dorazit",
        "dosahovat",
        "doslova",
        "dospělý",
        "dost",
        "dostat",
        "dostatečný",
        "dostatečně",
        "dostupný",
        "dostávat",
        "dosud",
        "dosáhnout",
        "dotace",
        "dotknout",
        "doufat",
        "dovnitř",
        "dovolená",
        "dovolit",
        "dovést",
        "dozvědět",
        "dočkat",
        "drahý",
        "drobný",
        "druh",
        "druhý",
        "dráha",
        "držet",
        "duben",
        "duch",
        "duše",
        "dva",
        "dvacet",
        "dvakrát",
        "dvanáct",
        "dveře",
        "dvůr",
        "dále",
        "dáma",
        "dát",
        "dávat",
        "dávka",
        "dávno",
        "dávný",
        "délka",
        "déšť",
        "díky",
        "díl",
        "dílo",
        "díra",
        "dít",
        "dítě",
        "dívat",
        "dívka",
        "dějiny",
        "děkovat",
        "dělat",
        "dětský",
        "dětství",
        "dřevo",
        "dřevěný",
        "důkaz",
        "důležitý",
        "dům",
        "důsledek",
        "důvod",
        "ekonomický",
        "ekonomika",
        "elektrický",
        "energetický",
        "energie",
        "euro",
        "Evropa",
        "evropský",
        "existence",
        "existovat",
        "fakt",
        "faktor",
        "fakulta",
        "fanoušek",
        "festival",
        "film",
        "filmový",
        "finance",
        "finanční",
        "firma",
        "fond",
        "forma",
        "fotbal",
        "fotbalový",
        "fotka",
        "fotografie",
        "Francie",
        "francouzský",
        "fungovat",
        "funkce",
        "fyzický",
        "fáze",
        "generace",
        "gól",
        "hala",
        "herec",
        "hezký",
        "historický",
        "historie",
        "hladina",
        "hlas",
        "hlava",
        "hlavní",
        "hlavně",
        "hledat",
        "hledisko",
        "hledět",
        "hluboký",
        "hmota",
        "hmotnost",
        "hned",
        "hnutí",
        "hnědý",
        "hodina",
        "hodit",
        "hodlat",
        "hodnocení",
        "hodnota",
        "hodně",
        "holka",
        "hora",
        "horký",
        "horní",
        "hospodářský",
        "host",
        "hotel",
        "hotový",
        "hovořit",
        "hra",
        "hrad",
        "hranice",
        "hrdina",
        "hrozit",
        "hrozně",
        "hrát",
        "hráč",
        "hudba",
        "hudební",
        "hvězda",
        "hřiště",
        "i",
        "ideální",
        "informace",
        "informační",
        "informovat",
        "instituce",
        "internet",
        "internetový",
        "investice",
        "italský",
        "jak",
        "jakmile",
        "jako",
        "jaký",
        "jakýkoli",
        "jakýsi",
        "jaro",
        "jasný",
        "jasně",
        "jazyk",
        "jeden",
        "jedinec",
        "jediný",
        "jednak",
        "jednat",
        "jednoduchý",
        "jednoduše",
        "jednotka",
        "jednotlivý",
        "jednou",
        "jednání",
        "jeho",
        "jejich",
        "její",
        "jelikož",
        "jemný",
        "jen",
        "jenom",
        "jenž",
        "jenže",
        "jestli",
        "jestliže",
        "jet",
        "jev",
        "jezdit",
        "ještě",
        "jinak",
        "jinde",
        "jiný",
        "jistota",
        "jistý",
        "jistě",
        "již",
        "jižní",
        "jmenovat",
        "jméno",
        "jo",
        "já",
        "jádro",
        "jídlo",
        "jíst",
        "jít",
        "jízda",
        "k",
        "kam",
        "kamarád",
        "kamenný",
        "kamera",
        "kancelář",
        "kapacita",
        "kapela",
        "kapitola",
        "kapitán",
        "kapsa",
        "kariéra",
        "karta",
        "kategorie",
        "každý",
        "kde",
        "kdo",
        "kdy",
        "kdyby",
        "kdykoli",
        "kdysi",
        "když",
        "kilometr",
        "klasický",
        "klid",
        "klidný",
        "klidně",
        "klient",
        "klub",
        "kluk",
        "klást",
        "klíč",
        "klíčový",
        "kniha",
        "knihovna",
        "knížka",
        "kolega",
        "kolem",
        "koleno",
        "kolik",
        "kolo",
        "kombinace",
        "komise",
        "komora",
        "komunikace",
        "konat",
        "koncert",
        "konec",
        "konečný",
        "konečně",
        "konkrétní",
        "konstrukce",
        "kontakt",
        "kontrola",
        "končit",
        "kopec",
        "koruna",
        "kost",
        "kostel",
        "koupit",
        "kousek",
        "kočka",
        "košile",
        "kraj",
        "krajina",
        "krajský",
        "krev",
        "krize",
        "krk",
        "krok",
        "kromě",
        "kruh",
        "král",
        "krása",
        "krásný",
        "krátce",
        "krátký",
        "který",
        "kuchyně",
        "kultura",
        "kulturní",
        "kurs",
        "kus",
        "kvalita",
        "kvalitní",
        "květ",
        "květen",
        "kvůli",
        "kámen",
        "káva",
        "křeslo",
        "křičet",
        "křídlo",
        "kůň",
        "kůže",
        "led",
        "leden",
        "lehce",
        "lehký",
        "les",
        "letadlo",
        "letní",
        "letos",
        "letošní",
        "levný",
        "levý",
        "ležet",
        "lidový",
        "lidský",
        "liga",
        "linka",
        "list",
        "listopad",
        "literatura",
        "lišit",
        "lokalita",
        "Londýn",
        "loď",
        "loňský",
        "lze",
        "láska",
        "látka",
        "lék",
        "lékař",
        "léto",
        "léčba",
        "líbit",
        "majetek",
        "majitel",
        "malý",
        "maminka",
        "manažer",
        "manžel",
        "manželka",
        "mapa",
        "maso",
        "materiál",
        "matka",
        "metoda",
        "metr",
        "mezi",
        "mezinárodní",
        "miliarda",
        "milimetr",
        "milión",
        "milovat",
        "milý",
        "mimo",
        "ministerstvo",
        "ministr",
        "minulost",
        "minulý",
        "minuta",
        "mistr",
        "mladík",
        "mladý",
        "mluvit",
        "mluvčí",
        "mléko",
        "mnohem",
        "mnoho",
        "mnohý",
        "množství",
        "mobil",
        "mobilní",
        "moc",
        "moci",
        "model",
        "moderní",
        "modrý",
        "moment",
        "Morava",
        "most",
        "motor",
        "mozek",
        "moře",
        "možnost",
        "možná",
        "možný",
        "mrtvý",
        "muset",
        "muzeum",
        "muž",
        "my",
        "mysl",
        "myslet",
        "myšlenka",
        "málo",
        "máma",
        "médium",
        "míra",
        "mírně",
        "místnost",
        "místní",
        "místo",
        "mít",
        "měnit",
        "město",
        "městský",
        "měsíc",
        "můj",
        "na",
        "nabídka",
        "nabídnout",
        "nabízet",
        "nacházet",
        "nad",
        "nadále",
        "naděje",
        "nahoru",
        "nahradit",
        "najednou",
        "najít",
        "nakonec",
        "nalézt",
        "naopak",
        "napadnout",
        "naposledy",
        "naprosto",
        "napsat",
        "napětí",
        "například",
        "narazit",
        "narodit",
        "nastat",
        "nastoupit",
        "natolik",
        "naučit",
        "navrhnout",
        "navzdory",
        "navíc",
        "navštívit",
        "nazývat",
        "naštěstí",
        "ne",
        "nebe",
        "nebezpečí",
        "nebo",
        "neboť",
        "nechat",
        "nechávat",
        "nedostatek",
        "nedávno",
        "neděle",
        "nehoda",
        "nejen",
        "nejprve",
        "nemoc",
        "nemocnice",
        "nemocný",
        "nepřítel",
        "neustále",
        "nezbytný",
        "než",
        "nic",
        "nicméně",
        "nijak",
        "nikdo",
        "nikdy",
        "nikoli",
        "no",
        "noc",
        "noha",
        "norma",
        "normální",
        "nos",
        "nosit",
        "novinka",
        "noviny",
        "novinář",
        "nový",
        "nově",
        "noční",
        "nutit",
        "nutný",
        "nyní",
        "nábytek",
        "nádherný",
        "náhle",
        "náhodou",
        "náklad",
        "nákup",
        "nálada",
        "náměstí",
        "nápad",
        "národ",
        "národní",
        "nárok",
        "náročný",
        "následek",
        "následně",
        "následovat",
        "následující",
        "nástroj",
        "návrat",
        "návrh",
        "návštěva",
        "návštěvník",
        "název",
        "názor",
        "náš",
        "nést",
        "nízký",
        "nýbrž",
        "něco",
        "nějak",
        "nějaký",
        "někde",
        "někdo",
        "někdy",
        "několik",
        "několikrát",
        "některý",
        "Němec",
        "Německo",
        "německý",
        "o",
        "oba",
        "obava",
        "obchod",
        "obchodní",
        "období",
        "obec",
        "obecný",
        "obecně",
        "objekt",
        "objem",
        "objevit",
        "objevovat",
        "oblast",
        "oblečení",
        "obličej",
        "oblíbený",
        "obor",
        "obr",
        "obrana",
        "obraz",
        "obrovský",
        "obrátit",
        "obrázek",
        "obsah",
        "obsahovat",
        "obvod",
        "obvykle",
        "obvyklý",
        "obyvatel",
        "obyčejný",
        "občan",
        "občanský",
        "občas",
        "oběť",
        "ochrana",
        "ocitnout",
        "od",
        "odborník",
        "odborný",
        "odchod",
        "odcházet",
        "oddělení",
        "odejít",
        "odhalit",
        "odjet",
        "odkud",
        "odlišný",
        "odmítat",
        "odmítnout",
        "odpoledne",
        "odpor",
        "odpovídat",
        "odpovědět",
        "odpověď",
        "oheň",
        "ohled",
        "okamžik",
        "okamžitě",
        "okno",
        "oko",
        "okolnost",
        "okolní",
        "okolo",
        "okolí",
        "okraj",
        "olej",
        "omezený",
        "on",
        "onemocnění",
        "onen",
        "oni",
        "opakovat",
        "opatření",
        "operace",
        "operační",
        "oprava",
        "opravdu",
        "oproti",
        "opustit",
        "opět",
        "organizace",
        "orgán",
        "osm",
        "osoba",
        "osobnost",
        "osobní",
        "osobně",
        "ostatní",
        "ostatně",
        "Ostrava",
        "ostrov",
        "ostrý",
        "osud",
        "otec",
        "otevřený",
        "otevřít",
        "otočit",
        "otázka",
        "ovlivnit",
        "ovšem",
        "označit",
        "označovat",
        "oznámit",
        "ozvat",
        "očekávat",
        "pacient",
        "padat",
        "padesát",
        "padnout",
        "pak",
        "pamatovat",
        "památka",
        "paměť",
        "pan",
        "paní",
        "papír",
        "parametr",
        "park",
        "partner",
        "patnáct",
        "patro",
        "patřit",
        "paže",
        "peníze",
        "pes",
        "pevný",
        "pevně",
        "pivo",
        "planeta",
        "platit",
        "plný",
        "plně",
        "plocha",
        "plyn",
        "Plzeň",
        "plán",
        "plánovat",
        "po",
        "pobyt",
        "pochopit",
        "pochopitelně",
        "pocházet",
        "pocit",
        "pod",
        "podat",
        "podařit",
        "podepsat",
        "podivný",
        "podlaha",
        "podle",
        "podmínka",
        "podnik",
        "podoba",
        "podobný",
        "podobně",
        "podpora",
        "podporovat",
        "podpořit",
        "podstata",
        "podstatný",
        "podzim",
        "podávat",
        "podíl",
        "podílet",
        "podívat",
        "pohled",
        "pohlédnout",
        "pohyb",
        "pohybovat",
        "pojem",
        "pokaždé",
        "pokoj",
        "pokoušet",
        "pokračovat",
        "pokud",
        "pokus",
        "pokusit",
        "pole",
        "policejní",
        "policie",
        "policista",
        "politický",
        "politik",
        "politika",
        "poloha",
        "polovina",
        "položit",
        "pomalu",
        "pomoc",
        "pomoci",
        "pomocí",
        "pomyslet",
        "pomáhat",
        "poměr",
        "poměrně",
        "poněkud",
        "popis",
        "popisovat",
        "poprvé",
        "popsat",
        "populace",
        "poradit",
        "posadit",
        "poskytnout",
        "poskytovat",
        "poslat",
        "poslední",
        "poslouchat",
        "postava",
        "postavení",
        "postavit",
        "postel",
        "postoj",
        "postup",
        "postupně",
        "potkat",
        "potom",
        "potravina",
        "potvrdit",
        "poté",
        "potíž",
        "potřeba",
        "potřebný",
        "potřebovat",
        "pouhý",
        "pouze",
        "použití",
        "použít",
        "používat",
        "povaha",
        "považovat",
        "povinnost",
        "povrch",
        "povést",
        "povídat",
        "povědět",
        "pozdní",
        "pozdě",
        "pozemek",
        "pozice",
        "pozitivní",
        "poznamenat",
        "poznat",
        "poznámka",
        "pozor",
        "pozornost",
        "pozorovat",
        "pozvat",
        "počasí",
        "počet",
        "počkat",
        "počátek",
        "počítat",
        "počítač",
        "pořád",
        "pořádek",
        "pořádně",
        "pořídit",
        "požadavek",
        "požádat",
        "prach",
        "pracovat",
        "pracovní",
        "pracovník",
        "Praha",
        "prakticky",
        "praktický",
        "pravda",
        "pravděpodobně",
        "pravidelný",
        "pravidelně",
        "pravidlo",
        "pravý",
        "praxe",
        "pražský",
        "premiér",
        "prezident",
        "princip",
        "pro",
        "problém",
        "probudit",
        "probíhat",
        "proběhnout",
        "procento",
        "proces",
        "procházet",
        "prodat",
        "prodej",
        "produkce",
        "produkt",
        "prodávat",
        "profesor",
        "program",
        "prohlásit",
        "projekt",
        "projev",
        "projevit",
        "projevovat",
        "projít",
        "promluvit",
        "proměnit",
        "prosinec",
        "prosit",
        "prostor",
        "prostě",
        "prostředek",
        "prostřednictvím",
        "prostředí",
        "proti",
        "proto",
        "protože",
        "proud",
        "provedení",
        "provoz",
        "provádět",
        "provést",
        "prozradit",
        "proč",
        "prst",
        "prvek",
        "první",
        "pryč",
        "práce",
        "právní",
        "právo",
        "právě",
        "prázdný",
        "prý",
        "průběh",
        "průmysl",
        "průměr",
        "průměrný",
        "psát",
        "pták",
        "ptát",
        "pustit",
        "pád",
        "pán",
        "pár",
        "pátek",
        "péče",
        "píseň",
        "pít",
        "pěkný",
        "pěkně",
        "pět",
        "přece",
        "před",
        "předchozí",
        "předem",
        "především",
        "předmět",
        "přednost",
        "přední",
        "předpoklad",
        "předpokládat",
        "předseda",
        "představa",
        "představení",
        "představit",
        "představovat",
        "předtím",
        "přejít",
        "překvapit",
        "přemýšlet",
        "přes",
        "přesný",
        "přesně",
        "přestat",
        "přesto",
        "přestože",
        "přesvědčit",
        "převzít",
        "přečíst",
        "přežít",
        "při",
        "přibližně",
        "přiblížit",
        "přicházet",
        "přidat",
        "přijet",
        "přijmout",
        "přijít",
        "přikývnout",
        "přinášet",
        "přinést",
        "připadat",
        "připojit",
        "připomenout",
        "připomínat",
        "připravený",
        "připravit",
        "připravovat",
        "přirozený",
        "přitom",
        "přivést",
        "přiznat",
        "přičemž",
        "přání",
        "přát",
        "příběh",
        "příjem",
        "příjemný",
        "příklad",
        "příležitost",
        "příliš",
        "přímo",
        "přímý",
        "případ",
        "případný",
        "případně",
        "příprava",
        "příroda",
        "přírodní",
        "příslušný",
        "příspěvek",
        "přístroj",
        "přístup",
        "přítel",
        "přítomnost",
        "přítomný",
        "příčina",
        "příští",
        "půda",
        "půl",
        "působení",
        "působit",
        "původ",
        "původní",
        "původně",
        "rada",
        "radnice",
        "radost",
        "rameno",
        "reagovat",
        "reakce",
        "realita",
        "realizace",
        "region",
        "regionální",
        "rekonstrukce",
        "republika",
        "restaurace",
        "ret",
        "reálný",
        "režim",
        "režisér",
        "riziko",
        "rodina",
        "rodinný",
        "rodič",
        "roh",
        "rok",
        "role",
        "román",
        "rostlina",
        "rovnice",
        "rovnou",
        "rovněž",
        "rozdíl",
        "rozdělit",
        "rozhodnout",
        "rozhodnutí",
        "rozhodně",
        "rozhodovat",
        "rozhovor",
        "rozměr",
        "rozpočet",
        "rozsah",
        "rozsáhlý",
        "rozumět",
        "rozvoj",
        "rozšířit",
        "ročník",
        "ruka",
        "Rusko",
        "ruský",
        "ryba",
        "rychle",
        "rychlost",
        "rychlý",
        "rád",
        "rámec",
        "rána",
        "ráno",
        "růst",
        "různý",
        "s",
        "samostatný",
        "samotný",
        "samozřejmě",
        "samý",
        "sbor",
        "sbírka",
        "schod",
        "schopnost",
        "schopný",
        "scéna",
        "sdružení",
        "sdělit",
        "se",
        "sedm",
        "sednout",
        "sedět",
        "sejít",
        "sem",
        "sen",
        "seriál",
        "sestra",
        "setkat",
        "setkání",
        "severní",
        "seznam",
        "seznámit",
        "sezona",
        "sice",
        "signál",
        "silnice",
        "silný",
        "silně",
        "situace",
        "skladba",
        "sklo",
        "skončit",
        "skoro",
        "skrývat",
        "skupina",
        "skutečnost",
        "skutečný",
        "skutečně",
        "skvělý",
        "skála",
        "slabý",
        "slavný",
        "sledovat",
        "slečna",
        "sloužit",
        "Slovensko",
        "slovenský",
        "slovo",
        "složitý",
        "složka",
        "slunce",
        "sluneční",
        "služba",
        "slyšet",
        "slza",
        "smlouva",
        "smrt",
        "smysl",
        "smát",
        "smích",
        "směr",
        "smět",
        "snad",
        "snadno",
        "snadný",
        "snaha",
        "snažit",
        "sníh",
        "snímek",
        "snížit",
        "sobota",
        "sociální",
        "sotva",
        "soubor",
        "soud",
        "souhlasit",
        "soukromý",
        "soupeř",
        "soused",
        "soustava",
        "soustředit",
        "soutěž",
        "souviset",
        "souvislost",
        "současnost",
        "současný",
        "současně",
        "součást",
        "spadnout",
        "spatřit",
        "specifický",
        "speciální",
        "spisovatel",
        "splnit",
        "spodní",
        "spojení",
        "spojený",
        "spojit",
        "spokojený",
        "společenský",
        "společnost",
        "společný",
        "společně",
        "spolu",
        "spolupráce",
        "spor",
        "sport",
        "sportovní",
        "spotřeba",
        "spousta",
        "spočívat",
        "správa",
        "správný",
        "správně",
        "spustit",
        "spánek",
        "spát",
        "spíš",
        "srdce",
        "srovnání",
        "srpen",
        "stanice",
        "stanovit",
        "starat",
        "starost",
        "starosta",
        "starý",
        "stav",
        "stavba",
        "stavební",
        "stavět",
        "stačit",
        "stejný",
        "stejně",
        "stihnout",
        "sto",
        "století",
        "stopa",
        "stovka",
        "strach",
        "strana",
        "strategie",
        "strašně",
        "stroj",
        "strom",
        "struktura",
        "stránka",
        "strávit",
        "student",
        "studený",
        "studie",
        "studium",
        "studovat",
        "stupeň",
        "styl",
        "stáhnout",
        "stále",
        "stát",
        "státní",
        "stávat",
        "stín",
        "stěna",
        "střecha",
        "střední",
        "stůl",
        "suchý",
        "svatý",
        "svaz",
        "svoboda",
        "svobodný",
        "svět",
        "světlo",
        "světový",
        "svůj",
        "symbol",
        "syn",
        "systém",
        "sál",
        "sám",
        "série",
        "síla",
        "síť",
        "sůl",
        "tabulka",
        "tady",
        "tajemství",
        "tajný",
        "tak",
        "takhle",
        "takový",
        "takto",
        "taky",
        "takzvaný",
        "také",
        "takže",
        "tam",
        "technický",
        "technika",
        "technologie",
        "teda",
        "tedy",
        "tehdejší",
        "tehdy",
        "telefon",
        "televize",
        "televizní",
        "temný",
        "ten",
        "tenhle",
        "tenkrát",
        "tento",
        "tentokrát",
        "tentýž",
        "teorie",
        "teplo",
        "teplota",
        "teplý",
        "teprve",
        "termín",
        "test",
        "text",
        "teď",
        "ticho",
        "tichý",
        "tisíc",
        "titul",
        "tiše",
        "tlak",
        "tlačítko",
        "tma",
        "tmavý",
        "to",
        "tolik",
        "totiž",
        "touha",
        "toužit",
        "tradice",
        "tradiční",
        "trasa",
        "trať",
        "trend",
        "trenér",
        "trest",
        "trh",
        "trochu",
        "trpět",
        "trvat",
        "tráva",
        "tu",
        "turnaj",
        "tušit",
        "tvar",
        "tvorba",
        "tvořit",
        "tvrdit",
        "tvrdý",
        "tvář",
        "tvůj",
        "ty",
        "typ",
        "typický",
        "tábor",
        "táhnout",
        "táta",
        "téma",
        "téměř",
        "též",
        "tón",
        "týden",
        "týkat",
        "tým",
        "týž",
        "tělo",
        "těsně",
        "těšit",
        "těžko",
        "těžký",
        "třeba",
        "třetina",
        "třetí",
        "tři",
        "třicet",
        "třída",
        "u",
        "ucho",
        "udržet",
        "udržovat",
        "událost",
        "udělat",
        "ukazovat",
        "ukázat",
        "ulice",
        "uložit",
        "umožnit",
        "umožňovat",
        "umístit",
        "umělec",
        "umělecký",
        "umělý",
        "umění",
        "umět",
        "unie",
        "univerzita",
        "upozornit",
        "uprostřed",
        "určený",
        "určit",
        "určitý",
        "určitě",
        "uskutečnit",
        "usmát",
        "usmívat",
        "utkání",
        "utéci",
        "uvažovat",
        "uvedený",
        "uvidět",
        "uvnitř",
        "uvádět",
        "uvést",
        "uvědomit",
        "uvědomovat",
        "uzavřít",
        "učinit",
        "učit",
        "učitel",
        "už",
        "uživatel",
        "užívat",
        "v",
        "vadit",
        "varianta",
        "vazba",
        "vedení",
        "vedle",
        "vedoucí",
        "vejít",
        "velice",
        "velikost",
        "veliký",
        "velký",
        "velmi",
        "ven",
        "venku",
        "verze",
        "vesmír",
        "vesnice",
        "večer",
        "večeře",
        "veřejnost",
        "veřejný",
        "veškerý",
        "vhodný",
        "viditelný",
        "vidět",
        "vina",
        "viset",
        "viz",
        "vlak",
        "vlas",
        "vlastnost",
        "vlastní",
        "vlastně",
        "vliv",
        "vlna",
        "vloni",
        "vláda",
        "vnitřní",
        "vnímat",
        "vnější",
        "voda",
        "vodní",
        "vojenský",
        "voják",
        "volat",
        "volba",
        "volit",
        "volný",
        "vozidlo",
        "vracet",
        "vrchol",
        "vrstva",
        "vrátit",
        "vstoupit",
        "vstup",
        "vstát",
        "vteřina",
        "vy",
        "vybavit",
        "vybraný",
        "vybrat",
        "vybírat",
        "vycházet",
        "vydat",
        "vydržet",
        "vydání",
        "vydávat",
        "vyhnout",
        "vyhrát",
        "vyjádřit",
        "vyjít",
        "vypadat",
        "vyprávět",
        "vyrazit",
        "vyrábět",
        "vyskytovat",
        "vysoko",
        "vysoký",
        "vystoupit",
        "vystupovat",
        "vysvětlit",
        "vysvětlovat",
        "vytvořit",
        "vytvářet",
        "vytáhnout",
        "využití",
        "využít",
        "využívat",
        "vyvolat",
        "vyzkoušet",
        "vyřešit",
        "vyžadovat",
        "vzduch",
        "vzdálenost",
        "vzdálený",
        "vzdát",
        "vzdělání",
        "vzdělávání",
        "vzhledem",
        "vznik",
        "vznikat",
        "vzniknout",
        "vzor",
        "vzpomenout",
        "vzpomínat",
        "vzpomínka",
        "vztah",
        "vzájemný",
        "vzít",
        "váha",
        "válka",
        "Vánoce",
        "vánoční",
        "váš",
        "vážný",
        "vážně",
        "vést",
        "víc",
        "více",
        "víkend",
        "víno",
        "víra",
        "vítr",
        "vítěz",
        "vítězství",
        "výbor",
        "výběr",
        "východ",
        "východní",
        "výchova",
        "výhoda",
        "výjimka",
        "výkon",
        "výměna",
        "výraz",
        "výrazný",
        "výrazně",
        "výroba",
        "výrobce",
        "výrobek",
        "výsledek",
        "výstava",
        "výstavba",
        "vývoj",
        "výzkum",
        "význam",
        "významný",
        "výzva",
        "výše",
        "výška",
        "včera",
        "včetně",
        "věc",
        "věda",
        "vědec",
        "vědecký",
        "vědomí",
        "vědět",
        "věk",
        "věnovat",
        "věta",
        "větev",
        "většina",
        "většinou",
        "vězení",
        "věřit",
        "věž",
        "však",
        "všechen",
        "všimnout",
        "všude",
        "vůbec",
        "vůle",
        "vůně",
        "vůz",
        "vůči",
        "vždy",
        "vždycky",
        "vždyť",
        "z",
        "za",
        "zabránit",
        "zabít",
        "zabývat",
        "zachovat",
        "zachránit",
        "zadní",
        "zahrada",
        "zahraniční",
        "zahraničí",
        "zahájit",
        "zajistit",
        "zajímat",
        "zajímavý",
        "zajít",
        "zakázka",
        "založit",
        "zamířit",
        "zaměstnanec",
        "zaměřit",
        "zaplatit",
        "zapomenout",
        "zas",
        "zase",
        "zasmát",
        "zastavit",
        "zasáhnout",
        "zatím",
        "zatímco",
        "zaujmout",
        "zavolat",
        "zavést",
        "zavřít",
        "zaznamenat",
        "začátek",
        "začínat",
        "začít",
        "zařízení",
        "zažít",
        "zbavit",
        "zboží",
        "zbraň",
        "zbytek",
        "zbýt",
        "zbývat",
        "zcela",
        "zda",
        "zde",
        "zdravotní",
        "zdraví",
        "zdravý",
        "zdroj",
        "zdát",
        "zejména",
        "zelený",
        "země",
        "zemřít",
        "zeptat",
        "zeď",
        "zhruba",
        "zima",
        "zimní",
        "zisk",
        "zjistit",
        "zkouška",
        "zkrátka",
        "zkusit",
        "zkušenost",
        "zlato",
        "zlatý",
        "zlý",
        "zmizet",
        "zmínit",
        "zmíněný",
        "změna",
        "změnit",
        "znak",
        "znalost",
        "znamenat",
        "značka",
        "značný",
        "znovu",
        "známý",
        "znát",
        "znít",
        "zpravidla",
        "zpráva",
        "zpátky",
        "zpívat",
        "zpět",
        "způsob",
        "způsobit",
        "zrovna",
        "ztratit",
        "ztrácet",
        "ztráta",
        "zub",
        "zvednout",
        "zvládnout",
        "zvláštní",
        "zvláště",
        "zvlášť",
        "zvolit",
        "zvuk",
        "zvyšovat",
        "zvíře",
        "zvýšení",
        "zvýšit",
        "záda",
        "zájem",
        "zákazník",
        "základ",
        "základní",
        "zákon",
        "záležet",
        "záležitost",
        "zámek",
        "západ",
        "západní",
        "zápas",
        "zároveň",
        "zásada",
        "zásadní",
        "zásah",
        "zástupce",
        "závislost",
        "závislý",
        "závod",
        "závěr",
        "záznam",
        "září",
        "zážitek",
        "získat",
        "zítra",
        "zřejmě",
        "zůstat",
        "zůstávat",
        "údaj",
        "úkol",
        "únor",
        "úplný",
        "úplně",
        "úprava",
        "úroveň",
        "úsek",
        "úsměv",
        "úspěch",
        "úspěšný",
        "ústa",
        "ústav",
        "útok",
        "útočník",
        "úvaha",
        "území",
        "úzký",
        "účast",
        "účastník",
        "účel",
        "účet",
        "účinek",
        "úřad",
        "úžasný",
        "čaj",
        "čas",
        "časopis",
        "časový",
        "často",
        "častý",
        "Čech",
        "Čechy",
        "čekat",
        "čelo",
        "černý",
        "čerstvý",
        "červen",
        "červenec",
        "červený",
        "Česko",
        "český",
        "či",
        "čin",
        "činit",
        "činnost",
        "čistý",
        "člen",
        "člověk",
        "článek",
        "čtenář",
        "čtvrtý",
        "čtyři",
        "část",
        "částice",
        "částka",
        "Čína",
        "čínský",
        "číslo",
        "číst",
        "řada",
        "ředitel",
        "řeka",
        "řeč",
        "řešení",
        "řešit",
        "řidič",
        "řád",
        "říci",
        "řídit",
        "říjen",
        "říkat",
        "řízení",
        "šance",
        "šaty",
        "šedý",
        "šest",
        "široký",
        "škoda",
        "škola",
        "školní",
        "špatný",
        "špatně",
        "štěstí",
        "šéf",
        "šťastný",
        "že",
        "žena",
        "ženský",
        "židle",
        "život",
        "životní",
        "živý",
        "žlutý",
        "žádat",
        "žádný",
        "žádost",
        "žák",
        "žít",
    )

    parts_of_speech: Dict[str, tuple] = {}
