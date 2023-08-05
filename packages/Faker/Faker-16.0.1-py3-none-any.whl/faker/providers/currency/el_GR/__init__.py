from .. import Provider as CurrencyProvider


class Provider(CurrencyProvider):
    # Source https://el.wikipedia.org/wiki/Κατάλογος_νομισμάτων_των_χωρών_του_κόσμου
    # Format: (code, name)
    currencies = (
        ("AED", "Ντιρχάμ των Ηνωμένων Αραβικών Εμιράτων"),
        ("AFN", "Αφγάνι"),
        ("ALL", "Λεκ"),
        ("AMD", "Ντραμ"),
        ("AOA", "Κουάνζα"),
        ("ARS", "Πέσο Αργεντινής"),
        ("AUD", "Δολάριο Αυστραλίας"),
        ("AZN", "Μανάτ του Αζερμπαϊτζάν"),
        ("BAM", "Μετατρέψιμο μάρκο Βοσνίας και Ερζεγοβίνης"),
        ("BBD", "Δολάριο των Μπαρμπάντος"),
        ("BDT", "Τάκα"),
        ("BGN", "Λεβ"),
        ("BHD", "Δηνάριο του Μπαχρέιν"),
        ("BIF", "Φράγκο του Μπουρούντι"),
        ("BND", "Κυάτ Μιανμάρ"),
        ("BOB", "Μπολιβιάνο"),
        ("BRL", "Ρεάλ Βραζιλίας"),
        ("BSD", "Δολάριο Μπαχάμας"),
        ("BTN", "Νγκούλντρουμ"),
        ("BWP", "Πούλα"),
        ("BYΝ", "Ρούβλι Λευκορωσίας"),
        ("BZD", "Δολάριο Μπελίζ"),
        ("CAD", "Δολάριο Καναδά"),
        ("CDF", "Φράγκο του Κονγκό"),
        ("CHF", "Ελβετικό Φράγκο"),
        ("CLP", "Πέσο Χιλής"),
        ("CNY", "Γιουάν |"),
        ("COP", "Πέσο Κολομβίας"),
        ("CRC", "Κολόν"),
        ("CSD", "Δηνάριο Σερβίας"),
        ("CUC", "Μετατρέψιμο πέσο Κούβας"),
        ("CUP", "Πέσος Κούβας"),
        ("CVE", "Εσκούδο Πρασίνου Ακρωτηρίου"),
        ("CZK", "Κορόνα Τσεχίας (koruna)"),
        ("DJF", "Φράγκο του Τζιμπουτί"),
        ("DKK", "Κορόνα Δανίας"),
        ("DOP", "Πέσο Δομινικανής Δημοκρατίας"),
        ("DZD", "Δηνάριο της Αλγερίας"),
        ("EGP", "Λίρα Αιγύπτου"),
        ("ERN", "Νάκφα"),
        ("ETB", "Μπιρ"),
        ("EUR", "Ευρώ"),
        ("FJD", "Δολάριο Νησιών Φίτζι"),
        ("GBP", "Στερλίνα"),
        ("GEL", "Λάρι"),
        ("GHC", "Σέντι της Γκάνας"),
        ("GMD", "Νταλάζι (Dalasi)"),
        ("GNF", "Φράγκο Γουινέας"),
        ("GTQ", "Κετσάλ"),
        ("GYD", "Δολάριο Γουιάνας"),
        ("HNL", "Λεμπίρα"),
        ("HRK", "Κούνα"),
        ("HTG", "Γκουρντ"),
        ("HUF", "Φιορίνι Ουγγαρίας"),
        ("IDR", "Ρουπία Ινδονησίας"),
        ("ILS", "Νέο σέκελ"),
        ("INR", "Ρουπία Ινδίας[6]"),
        ("IQD", "Δηνάριο του Ιράκ"),
        ("IRR", "Ριάλ του Ιράν"),
        ("ISK", "Κορόνα Ισλανδίας (króna)"),
        ("JMD", "Δολάριο Τζαμάικας"),
        ("JOD", "Ιορδανικό δηνάριο"),
        ("JPY", "Γιέν"),
        ("KES", "Σελίνι Κένυας"),
        ("KGS", "Σομ της Κιργιζίας"),
        ("KHR", "Ριέλ Καμπότζης"),
        ("KMF", "Φράγκο Κομόρων"),
        ("KPW", "Γουόν Βόρειας Κορέας"),
        ("KRW", "Γουόν Νότιας Κορέας"),
        ("KWD", "Δηνάριο του Κουβέιτ"),
        ("KZT", "Τένγκε"),
        ("LAK", "Κιπ"),
        ("LBP", "Λίρα Λιβάνου"),
        ("LKR", "Ρουπία της Σρι Λάνκας (rupee)"),
        ("LRD", "Δολάριο Λιβερίας"),
        ("LSL", "Λότι"),
        ("LYD", "Δηνάριο Λιβύης"),
        ("MAD", "Ντιρχάμ Μαρόκου"),
        ("MDL", "Μολδαβικό Λέου"),
        ("MGA", "Αριάρι[10]"),
        ("MKD", "Δηνάριο Βόρειας Μακεδονίας"),
        ("MNT", "Τουγκρίκ"),
        ("MRU", "Ουγκίγια[10]"),
        ("MUR", "Ρουπία Μαυρίκιου"),
        ("MVR", "Ρουφίγια"),
        ("MWK", "Κουάτσα του Μαλάουι"),
        ("MXN", "Πέσο Μεξικού"),
        ("MYR", "Ρινγκίτ"),
        ("MZN", "Μετικάλ"),
        ("NAD", "Δολάριο Ναμίμπιας"),
        ("NGN", "Νάιρα"),
        ("NIO", "Χρυσό κόρντομπα της Νικαράγουας"),
        ("NOK", "Κορόνα Νορβηγίας (krone)"),
        ("NPR", "Ρουπία του Νεπάλ (rupee)"),
        ("NZD", "Δολάριο Νέας Ζηλανδίας"),
        ("OMR", "Ριάλ του Ομάν"),
        ("PAB", "Μπαλμπόα Παναμά"),
        ("PEK", "ΠΕΚΕΡΟΝ"),
        ("PEN", "Σολ Περού (sol)"),
        ("PGK", "Κίνα Παπούα-Νέας Γουινέας"),
        ("PHP", "Πέσο Φιλιππίνων"),
        ("PKR", "Ρουπία του Πακιστάν (rupee)"),
        ("PLN", "Ζλότι"),
        ("PYG", "Γκουαρανί"),
        ("QAR", "Ριγιάλ του Κατάρ"),
        ("RON", "Λέου Ρουμανίας"),
        ("RUB", "Ρούβλι Ρωσίας"),
        ("RWF", "Φράγκο της Ρουάντα"),
        ("SAR", "Ριάλ Σαουδικής Αραβίας (riyal)"),
        ("SBD", "Δολάριο των Νήσων του Σολομώντα"),
        ("SCR", "Ρουπία των Σεϋχελλών (Seychellois rupee)"),
        ("SDG", "Λίρα του Σουδάν"),
        ("SEK", "Κορόνα Σουηδίας (krona)"),
        ("SGD", "Δολάριο Σιγκαπούρης"),
        ("SLL", "Λεόνε της Σιέρα Λεόνε"),
        ("SOS", "Σελίνι Σομαλίας"),
        ("SRD", "Δολάριο του Σουρινάμ"),
        ("SSP", "Λίρα Νοτίου Σουδάν"),
        ("STN", "Ντόμπρα"),
        ("SYP", "Λίρα Συρίας"),
        ("SZL", "Λιλανγκένι"),
        ("THB", "Μπαχτ"),
        ("TJS", "Σομόνι"),
        ("TMM", "Μανάτ του Τουρκμενιστάν"),
        ("TND", "Δηνάριο Τυνησίας"),
        ("TOP", "Παάνγκα"),
        ("TRY", "Τουρκική Λίρα"),
        ("TTD", "Δολάριο Τρινιντάντ και Τομπάγκο"),
        ("TZS", "Σελίνι Τανζανίας (shilling)"),
        ("UAH", "Γρίβνα Ουκρανίας"),
        ("UGX", "Σελίνι Ουγκάντας"),
        ("USD", "Δολάριο ΗΠΑ"),
        ("UYU", "Πέσο Ουρουγουάης"),
        ("UZS", "Σομ του Ουζμπεκιστάν"),
        ("VES", "Μπολίβαρ Σομπεράνο"),
        ("VND", "Ντονγκ"),
        ("VUV", "Βάτου"),
        ("WST", "Τάλα Σαμόα"),
        ("XAF", "Φράγκο CFA Κεντρικής Αφρικής"),
        ("XCD", "Δολάριο Ανατολικής Καραϊβικής"),
        ("XOF", "Φράγκο CFA Δυτικής Αφρικής"),
        ("YER", "Ριάλ Υεμένης"),
        ("ZAR", "Ραντ Νότιας Αφρικής"),
        ("ZMK", "Κουάτσα της Ζάμπιας"),
        ("ZWD", "RTGS Dollar"),
    )

    price_formats = ["#,##", "%#,##", "%##,##", "%.###,##", "%#.###,##"]

    def pricetag(self) -> str:
        return self.numerify(self.random_element(self.price_formats)) + "\N{no-break space}\N{euro sign}"
