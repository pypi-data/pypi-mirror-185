from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{first_name}} {{last_name}}",
        "{{prefix}} {{first_name}} {{last_name}}",
    )

    prefixes_male = (
        "GEN",
        "LT GEN",
        "MAJ GEN",
        "COL",
        "LT COL",
        "MAJ",
        "CAPT",
        "LT",
        "SUB LT",
        "S M 1",
        "S M 2",
        "S M 3",
        "SGT",
        "CPL",
        "PFC",
        "PVT",
        "ADM",
        "V ADM",
        "R ADM",
        "CAPT",
        "CDR",
        "L CDR",
        "LT",
        "LT JG",
        "SUB LT",
        "CPO 1",
        "CPO 2",
        "CPO 3",
        "PO 1",
        "PO 2",
        "PO 3",
        "SEA-MAN",
        "ACM",
        "AM",
        "AVM",
        "GP CAPT",
        "WG CDR",
        "SQN LDR",
        "FLT LT",
        "FLG OFF",
        "PLT OFF",
        "FS 1",
        "FS 2",
        "FS 3",
        "SGT",
        "CPL",
        "LAC",
        "AMN",
        "POL GEN",
        "POL LT GEN",
        "POL MAJ GEN",
        "POL COL",
        "POL LT COL",
        "POL MAJ",
        "POL CAPT",
        "POL LT",
        "POL SUB LT",
        "POL SEN SGT MAJ",
        "POL SGT MAJ",
        "POL SGT",
        "POL CPL",
        "POL L/C",
        "POL CONST",
        "MR",
        "REV",
        "M L",
        "M R",
        "SAMANERA",
        "PHRA",
        "PHRA ATHIKAN",
        "CHAO ATHIKAN",
        "PHRAPALAD",
        "PHRASAMU",
        "PHRABAIDIKA",
        "PHRAKHU PALAD",
        "PHRAKHU SAMU",
        "PHRAKHU BAIDIKA",
        "PHRAMAHA",
        "PHRAKHU DHAMMADHORN",
        "PHRAKHU VINAIDHORN",
    )

    prefixes_female = (
        "GEN",
        "LT GEN",
        "MAJ GEN",
        "COL",
        "LT COL",
        "MAJ",
        "CAPT",
        "LT",
        "SUB LT",
        "S M 1",
        "S M 2",
        "S M 3",
        "SGT",
        "CPL",
        "PFC",
        "PVT",
        "ADM",
        "V ADM",
        "R ADM",
        "CAPT",
        "CDR",
        "L CDR",
        "LT",
        "LT JG",
        "SUB LT",
        "CPO 1",
        "CPO 2",
        "CPO 3",
        "PO 1",
        "PO 2",
        "PO 3",
        "SEA-MAN",
        "ACM",
        "AM",
        "AVM",
        "GP CAPT",
        "WG CDR",
        "SQN LDR",
        "FLT LT",
        "FLG OFF",
        "PLT OFF",
        "FS 1",
        "FS 2",
        "FS 3",
        "SGT",
        "CPL",
        "LAC",
        "AMN",
        "POL GEN",
        "POL LT GEN",
        "POL MAJ GEN",
        "POL COL",
        "POL LT COL",
        "POL MAJ",
        "POL CAPT",
        "POL LT",
        "POL SUB LT",
        "POL SEN SGT MAJ",
        "POL SGT MAJ",
        "POL SGT",
        "POL CPL",
        "POL L/C",
        "POL CONST",
        "MRS",
        "MISS",
        "REV",
        "M L",
    )

    prefixes = prefixes_male + prefixes_female

    first_names = (
        "Pornchanok",
        "Patchaploy",
        "Peem",
        "Kodchaporn",
        "Pattapon",
        "Sarunporn",
        "Jinjuta",
        "Sorawut",
        "Suvakit",
        "Prima",
        "Darin",
        "Pintusorn",
        "Kulnun",
        "Nutcha",
        "Nutkrita",
        "Sittikorn",
        "Wasin",
        "Apisara",
        "Nattawun",
        "Tunradee",
        "Niracha",
        "Tunchanok",
        "Kamolchanok",
        "Jaruwan",
        "Pachongruk",
        "Pakjira",
        "Pattatomporn",
        "Suwijuk",
        "Noppakao",
        "Ratchanon",
        "Atit",
        "Kunaporn",
        "Arisara",
        "Todsawun",
        "Chaiwut",
        "Puntira",
        "Supasita",
        "Patcharaporn",
        "Phubes",
        "Pattamon",
        "Chanya",
        "Pannawich",
        "Chawin",
        "Pada",
        "Chanikan",
        "Nutwadee",
        "Chalisa",
        "Prames",
        "Supasit",
        "Sitiwat",
        "Teetat",
        "Yada",
        "Phenphitcha",
        "Anon",
        "Chaifah",
        "Pawan",
        "Aunyaporn",
        "Yanisa",
        "Pak",
        "Chayanin",
        "Chayapat",
        "Jitrin",
        "Wassaya",
        "Pitipat",
        "Nichakarn",
        "Parin",
        "Thanatcha",
    )

    last_names = (
        "Prachayaroch",
        "Prachayaroch",
        "Kamalanon",
        "Tianvarich",
        "Bunlerngsri",
        "Sukhenai",
        "Posalee",
        "Chaisatit",
        "Sujjaboriboon",
        "Kamalanon",
        "Neerachapong",
        "Pianduangsri",
        "Pasuk",
        "Losatapornpipit",
        "Suraprasert",
        "Matinawin",
        "Choeychuen",
        "Wasunun",
        "Kumsoontorn",
        "Sireelert",
        "Boonpungbaramee",
        "Sorattanachai",
        "Benchapatranon",
        "Intaum",
        "Pikatsingkorn",
        "Srisoontorn",
        "Polpo",
        "Kongchayasukawut",
        "Charoensuksopol",
        "Bunlupong",
        "Chomsri",
        "Tungkasethakul",
        "Chowitunkit",
        "Todsapornpitakul",
        "Wimolnot",
        "Kittakun",
        "Methavorakul",
        "Pitanuwat",
        "Phusilarungrueng",
        "Turongkinanon",
        "Kitprapa",
        "Pothanun",
        "Youprasert",
        "Methavorakul",
        "Vethayasas",
        "Sooksawang",
        "Anekvorakul",
        "Pichpandecha",
        "Sittisaowapak",
        "Suraprachit",
        "Kongsri",
        "Trikasemmart",
        "Habpanom",
        "Wannapaitoonsri",
        "Vinyuvanichkul",
        "Pongpanitch",
        "Permchart",
        "Chaihirankarn",
        "Thantananont",
        "Norramon",
        "Prayoonhong",
        "Lertsattayanusak",
        "Polauaypon",
        "Prakalpawong",
        "Titipatrayunyong",
        "Krittayanukoon",
        "Siripaiboo",
    )
