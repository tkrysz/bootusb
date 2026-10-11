LANGS = {"pl": "Polski", "en": "English", "de": "Deutsch"}
DEFAULT_LANG = "pl"

# Teksty interfejsu strony
UI = {
    "pl": {
        "title": "Multiboot USB Guide",
        "hero_title": "Jak stworzyć Multiboot USB?",
        "hero_lead": "Przewodnik po najlepszych metodach na jeden pendrive z wieloma systemami.",
        "pros": "Zalety:",
        "cons": "Wady:",
        "platform": "Platforma",
        "instructions": "Instrukcja krok po kroku",
        "modal_title": "tworzenie bootowalnego pendrive",
        "close": "Zamknij",
        "warning_label": "Uwaga:",
        "warning": "tworzenie bootowalnego pendrive usuwa wszystkie dane z nośnika. Zrób kopię zapasową. "
                   "Pobieraj programy tylko z oficjalnych stron i, jeśli to możliwe, weryfikuj sumy kontrolne plików ISO.",
        "summary_title": "Podsumowanie - co wybrać?",
        "col_method": "Metoda",
        "col_use": "Główne zastosowanie",
        "col_level": "Poziom trudności",
        "language": "Język",
    },
    "en": {
        "title": "Multiboot USB Guide",
        "hero_title": "How to create a Multiboot USB?",
        "hero_lead": "A guide to the best ways to put multiple operating systems on a single flash drive.",
        "pros": "Pros:",
        "cons": "Cons:",
        "platform": "Platform",
        "instructions": "Step-by-step instructions",
        "modal_title": "creating a bootable USB drive",
        "close": "Close",
        "warning_label": "Warning:",
        "warning": "creating a bootable USB drive erases all data on the device. Make a backup first. "
                   "Download tools only from official websites and, if possible, verify the checksums of ISO files.",
        "summary_title": "Summary - which one to choose?",
        "col_method": "Method",
        "col_use": "Main use case",
        "col_level": "Difficulty",
        "language": "Language",
    },
    "de": {
        "title": "Multiboot-USB-Anleitung",
        "hero_title": "Wie erstellt man einen Multiboot-USB-Stick?",
        "hero_lead": "Ein Leitfaden zu den besten Methoden, mehrere Betriebssysteme auf einem USB-Stick unterzubringen.",
        "pros": "Vorteile:",
        "cons": "Nachteile:",
        "platform": "Plattform",
        "instructions": "Schritt-für-Schritt-Anleitung",
        "modal_title": "bootfähigen USB-Stick erstellen",
        "close": "Schließen",
        "warning_label": "Achtung:",
        "warning": "Beim Erstellen eines bootfähigen USB-Sticks werden alle Daten auf dem Datenträger gelöscht. "
                   "Erstellen Sie vorher ein Backup. Laden Sie Programme nur von den offiziellen Webseiten herunter "
                   "und prüfen Sie nach Möglichkeit die Prüfsummen der ISO-Dateien.",
        "summary_title": "Zusammenfassung - was wählen?",
        "col_method": "Methode",
        "col_use": "Haupteinsatzzweck",
        "col_level": "Schwierigkeitsgrad",
        "language": "Sprache",
    },
}

# Dane niezależne od języka: id, nazwa, adresy (w URL {lang} jest podmieniane na kod języka)
METHODS = [
    {
        "id": "ventoy",
        "name": "Ventoy",
        "links": [
            {"key": "site", "url": "https://www.ventoy.net/{lang}/index.html"},
            {"key": "download", "url": "https://github.com/ventoy/Ventoy/releases", "primary": True},
        ],
    },
    {
        "id": "yumi",
        "name": "YUMI (Your Universal Multiboot Installer)",
        "links": [
            {"key": "download", "url": "https://pendrivelinux.com/yumi-multiboot-usb-creator/", "primary": True},
        ],
    },
    {
        "id": "winsetup",
        "name": "WinSetupFromUSB",
        "links": [
            {"key": "download", "url": "https://www.winsetupfromusb.com/downloads/", "primary": True},
        ],
    },
    {
        "id": "rufus",
        "name": "Rufus (Single Boot/Manual)",
        "links": [
            {"key": "download", "url": "https://rufus.ie/{lang}/", "primary": True},
            {"key": "github", "url": "https://github.com/pbatard/rufus/releases"},
        ],
    },
]

LINK_LABELS = {
    "pl": {"site": "Strona projektu", "download": "Pobierz", "github": "GitHub"},
    "en": {"site": "Project website", "download": "Download", "github": "GitHub"},
    "de": {"site": "Projektseite", "download": "Herunterladen", "github": "GitHub"},
}

# Teksty opisowe poszczególnych metod
CONTENT = {
    "pl": {
        "ventoy": {
            "difficulty": "Bardzo łatwa",
            "description": "Rewolucyjna metoda. Instalujesz Ventoy na pendrive raz, a potem po prostu przeciągasz pliki .ISO na dysk jak zwykłe pliki.",
            "pros": ["Najszybsza metoda", "Można mieszać systemy", "Brak konieczności formatowania po dodaniu ISO"],
            "cons": ["Wymaga wsparcia UEFI/Legacy w specyficzny sposób"],
            "platform": "Windows, Linux",
            "use": "Dla każdego (najwygodniejsza)",
            "level": "Bardzo niski",
            "steps": [
                "Pobierz najnowszą wersję Ventoy (ventoy-x.y.z-windows.zip) i rozpakuj archiwum.",
                "Podłącz pendrive (zrób kopię danych – instalacja go sformatuje).",
                "Uruchom Ventoy2Disk.exe (na Linuksie: sudo sh Ventoy2Disk.sh -i /dev/sdX).",
                "Wybierz pendrive z listy <em>Device</em>. W menu <em>Option → Partition Style</em> wybierz GPT dla nowszych komputerów UEFI lub MBR dla starszych.",
                "Kliknij <em>Install</em> i dwukrotnie potwierdź ostrzeżenie o utracie danych.",
                "Po zakończeniu na pendrive pojawi się partycja <em>Ventoy</em>. Skopiuj na nią pliki .ISO (Windows, Linux, narzędzia) zwykłym kopiowaniem.",
                "Uruchom komputer z pendrive (klawisz wyboru bootowania: F12, F10, Esc lub F8 – zależnie od producenta) i wybierz obraz z menu Ventoy.",
            ],
        },
        "yumi": {
            "difficulty": "Średnia",
            "description": "Klasyczne narzędzie, które pozwala wybrać systemy z listy podczas procesu tworzenia pendrive'a.",
            "pros": ["Bardzo stabilna", "Duża biblioteka systemów", "Działa świetnie na starszych komputerach"],
            "cons": ["Konieczność ponownego uruchomienia programu przy dodawaniu nowych systemów"],
            "platform": "Windows, Linux",
            "use": "Dla fanów klasycznych narzędzi",
            "level": "Średni",
            "steps": [
                "Pobierz YUMI (wersja <em>exFAT</em> dla plików ISO powyżej 4 GB i systemów UEFI, wersja BIOS dla starszych komputerów) – instalacja nie jest wymagana.",
                "Podłącz pendrive i uruchom plik YUMI jako administrator.",
                "Zaakceptuj licencję i wybierz literę pendrive w kroku 1.",
                "W kroku 2 wybierz dystrybucję z listy (np. Ubuntu). Zaznacz opcję formatowania przy pierwszym użyciu.",
                "W kroku 3 wskaż pobrany plik ISO (lub użyj opcji <em>Download the ISO</em>), po czym kliknij <em>Create</em>.",
                "Po zakończeniu YUMI zapyta, czy dodać kolejny system – potwierdź i powtórz kroki 2–3 dla każdego kolejnego ISO.",
                "Uruchom komputer z pendrive i wybierz system z menu startowego.",
            ],
        },
        "winsetup": {
            "difficulty": "Średnia",
            "description": "Specjalistyczne narzędzie skupiające się głównie na instalatorach systemów Windows (XP, 7, 8, 10, 11).",
            "pros": ["Najlepsza do systemów Windows", "Obsługuje bardzo stare standardy"],
            "cons": ["Mniej intuicyjna dla systemów Linux"],
            "platform": "Windows",
            "use": "Naprawa/Instalacja Windows",
            "level": "Średni",
            "steps": [
                "Pobierz WinSetupFromUSB, uruchom samorozpakowujące się archiwum i wybierz wersję 64-bitową (WinSetupFromUSB_x64.exe).",
                "Podłącz pendrive i wybierz go w polu <em>USB disk selection</em>.",
                "Zaznacz <em>Auto format it with FBinst</em> (wybierz FAT32; dla ISO powyżej 4 GB – NTFS, ale wtedy tylko tryb BIOS/Legacy).",
                "Zaznacz sekcję systemu, który dodajesz (np. <em>Vista/7/8/10/11/Server</em>) i wskaż plik ISO przyciskiem <em>…</em>. Dla Linuksa użyj sekcji <em>Linux ISO/Other Grub4dos compatible ISO</em>.",
                "Kliknij <em>GO</em> i potwierdź ostrzeżenia. Poczekaj na komunikat <em>Job done</em>.",
                "Kolejne systemy dodajesz, uruchamiając program ponownie – tym razem <b>bez</b> zaznaczania formatowania.",
                "Przetestuj pendrive w emulatorze QEMU (opcja <em>Test in QEMU</em>) lub uruchom z niego komputer.",
            ],
        },
        "rufus": {
            "difficulty": "Łatwa",
            "description": "Choć Rufus służy głównie do jednego systemu, można go użyć do przygotowania bazy pod bardziej zaawansowane metody.",
            "pros": ["Niezawodność", "Szybkość"],
            "cons": ["Brak natywnego wsparcia dla multiboot"],
            "platform": "Windows",
            "use": "Pendrive z jednym systemem",
            "level": "Niski",
            "steps": [
                "Pobierz Rufus (wersja przenośna nie wymaga instalacji) i uruchom go.",
                "Podłącz pendrive – zostanie wykryty automatycznie w polu <em>Urządzenie</em> (kopia danych obowiązkowa, dysk zostanie wyczyszczony).",
                "Kliknij <em>WYBIERZ</em> i wskaż plik ISO systemu.",
                "Wybierz schemat partycji: <em>GPT</em> dla UEFI lub <em>MBR</em> dla BIOS/Legacy (Rufus podpowie wartość dla danego obrazu).",
                "Kliknij <em>START</em>, w razie pytania wybierz tryb zapisu obrazu ISO i potwierdź.",
                "Uruchom komputer z pendrive. Aby uzyskać multiboot, możesz w ten sposób zrobić pendrive z jednym systemem albo użyć Ventoy.",
            ],
        },
    },
    "en": {
        "ventoy": {
            "difficulty": "Very easy",
            "description": "A revolutionary method. You install Ventoy on the flash drive once, and from then on you simply drag and drop .ISO files onto it like ordinary files.",
            "pros": ["Fastest method", "Mix different operating systems", "No need to reformat after adding an ISO"],
            "cons": ["Needs UEFI/Legacy support in a specific way"],
            "platform": "Windows, Linux",
            "use": "Everyone (the most convenient)",
            "level": "Very low",
            "steps": [
                "Download the latest Ventoy release (ventoy-x.y.z-windows.zip) and extract the archive.",
                "Plug in the USB drive (back up your data – the installation will format it).",
                "Run Ventoy2Disk.exe (on Linux: sudo sh Ventoy2Disk.sh -i /dev/sdX).",
                "Select your drive in the <em>Device</em> list. In <em>Option → Partition Style</em> choose GPT for modern UEFI computers or MBR for older ones.",
                "Click <em>Install</em> and confirm the data-loss warning twice.",
                "When it finishes, a <em>Ventoy</em> partition appears on the drive. Copy your .ISO files (Windows, Linux, utilities) onto it like regular files.",
                "Boot the computer from the USB drive (boot menu key: F12, F10, Esc or F8 – depends on the manufacturer) and pick an image from the Ventoy menu.",
            ],
        },
        "yumi": {
            "difficulty": "Medium",
            "description": "A classic tool that lets you pick systems from a list while the flash drive is being created.",
            "pros": ["Very stable", "Large library of systems", "Works great on older computers"],
            "cons": ["You must run the program again each time you add a new system"],
            "platform": "Windows, Linux",
            "use": "For fans of classic tools",
            "level": "Medium",
            "steps": [
                "Download YUMI (the <em>exFAT</em> version for ISO files over 4 GB and UEFI systems, the BIOS version for older computers) – no installation required.",
                "Plug in the USB drive and run YUMI as administrator.",
                "Accept the license and select the drive letter in step 1.",
                "In step 2 choose a distribution from the list (e.g. Ubuntu). Tick the format option on first use.",
                "In step 3 point to the downloaded ISO file (or use <em>Download the ISO</em>), then click <em>Create</em>.",
                "When done, YUMI asks whether to add another system – confirm and repeat steps 2–3 for each additional ISO.",
                "Boot the computer from the USB drive and choose a system from the boot menu.",
            ],
        },
        "winsetup": {
            "difficulty": "Medium",
            "description": "A specialist tool focused mainly on Windows installers (XP, 7, 8, 10, 11).",
            "pros": ["Best for Windows systems", "Supports very old standards"],
            "cons": ["Less intuitive for Linux systems"],
            "platform": "Windows",
            "use": "Repairing/installing Windows",
            "level": "Medium",
            "steps": [
                "Download WinSetupFromUSB, run the self-extracting archive and pick the 64-bit version (WinSetupFromUSB_x64.exe).",
                "Plug in the USB drive and select it in the <em>USB disk selection</em> field.",
                "Tick <em>Auto format it with FBinst</em> (choose FAT32; for ISO files over 4 GB use NTFS, but then only BIOS/Legacy mode works).",
                "Tick the section for the system you are adding (e.g. <em>Vista/7/8/10/11/Server</em>) and select the ISO file with the <em>…</em> button. For Linux use the <em>Linux ISO/Other Grub4dos compatible ISO</em> section.",
                "Click <em>GO</em> and confirm the warnings. Wait for the <em>Job done</em> message.",
                "To add more systems, run the program again – this time <b>without</b> ticking the format option.",
                "Test the drive in the QEMU emulator (<em>Test in QEMU</em> option) or boot a computer from it.",
            ],
        },
        "rufus": {
            "difficulty": "Easy",
            "description": "Although Rufus is mainly meant for a single system, it can be used to prepare a base for more advanced methods.",
            "pros": ["Reliable", "Fast"],
            "cons": ["No native multiboot support"],
            "platform": "Windows",
            "use": "A drive with a single system",
            "level": "Low",
            "steps": [
                "Download Rufus (the portable version needs no installation) and run it.",
                "Plug in the USB drive – it is detected automatically in the <em>Device</em> field (a backup is a must, the drive will be wiped).",
                "Click <em>SELECT</em> and choose the system's ISO file.",
                "Choose the partition scheme: <em>GPT</em> for UEFI or <em>MBR</em> for BIOS/Legacy (Rufus suggests a value for the given image).",
                "Click <em>START</em>, choose ISO image mode if asked, and confirm.",
                "Boot the computer from the USB drive. For multiboot you can use this to make a single-system drive, or use Ventoy instead.",
            ],
        },
    },
    "de": {
        "ventoy": {
            "difficulty": "Sehr einfach",
            "description": "Eine revolutionäre Methode. Sie installieren Ventoy einmal auf dem USB-Stick und ziehen danach einfach .ISO-Dateien wie normale Dateien darauf.",
            "pros": ["Schnellste Methode", "Verschiedene Systeme mischbar", "Kein erneutes Formatieren nach dem Hinzufügen einer ISO nötig"],
            "cons": ["Benötigt UEFI-/Legacy-Unterstützung auf spezielle Weise"],
            "platform": "Windows, Linux",
            "use": "Für jeden (am bequemsten)",
            "level": "Sehr niedrig",
            "steps": [
                "Laden Sie die neueste Ventoy-Version (ventoy-x.y.z-windows.zip) herunter und entpacken Sie das Archiv.",
                "Stecken Sie den USB-Stick an (sichern Sie Ihre Daten – die Installation formatiert ihn).",
                "Starten Sie Ventoy2Disk.exe (unter Linux: sudo sh Ventoy2Disk.sh -i /dev/sdX).",
                "Wählen Sie den Stick in der Liste <em>Device</em> aus. Wählen Sie unter <em>Option → Partition Style</em> GPT für neuere UEFI-Rechner oder MBR für ältere.",
                "Klicken Sie auf <em>Install</em> und bestätigen Sie die Warnung vor Datenverlust zweimal.",
                "Danach erscheint auf dem Stick eine Partition <em>Ventoy</em>. Kopieren Sie Ihre .ISO-Dateien (Windows, Linux, Tools) einfach dorthin.",
                "Starten Sie den Rechner vom USB-Stick (Boot-Menü-Taste: F12, F10, Esc oder F8 – je nach Hersteller) und wählen Sie ein Image im Ventoy-Menü aus.",
            ],
        },
        "yumi": {
            "difficulty": "Mittel",
            "description": "Ein klassisches Tool, mit dem Sie beim Erstellen des USB-Sticks Systeme aus einer Liste auswählen.",
            "pros": ["Sehr stabil", "Große Auswahl an Systemen", "Funktioniert hervorragend auf älteren Rechnern"],
            "cons": ["Das Programm muss für jedes neue System erneut gestartet werden"],
            "platform": "Windows, Linux",
            "use": "Für Fans klassischer Tools",
            "level": "Mittel",
            "steps": [
                "Laden Sie YUMI herunter (die <em>exFAT</em>-Version für ISO-Dateien über 4 GB und UEFI-Systeme, die BIOS-Version für ältere Rechner) – eine Installation ist nicht nötig.",
                "Stecken Sie den USB-Stick an und starten Sie YUMI als Administrator.",
                "Akzeptieren Sie die Lizenz und wählen Sie in Schritt 1 den Laufwerksbuchstaben des Sticks.",
                "Wählen Sie in Schritt 2 eine Distribution aus der Liste (z. B. Ubuntu). Aktivieren Sie bei der ersten Verwendung die Formatierungsoption.",
                "Geben Sie in Schritt 3 die heruntergeladene ISO-Datei an (oder nutzen Sie <em>Download the ISO</em>) und klicken Sie auf <em>Create</em>.",
                "Anschließend fragt YUMI, ob ein weiteres System hinzugefügt werden soll – bestätigen Sie und wiederholen Sie die Schritte 2–3 für jede weitere ISO.",
                "Starten Sie den Rechner vom USB-Stick und wählen Sie ein System im Startmenü.",
            ],
        },
        "winsetup": {
            "difficulty": "Mittel",
            "description": "Ein Spezialwerkzeug, das sich vor allem auf Windows-Installationsmedien (XP, 7, 8, 10, 11) konzentriert.",
            "pros": ["Am besten für Windows-Systeme", "Unterstützt sehr alte Standards"],
            "cons": ["Für Linux-Systeme weniger intuitiv"],
            "platform": "Windows",
            "use": "Windows reparieren/installieren",
            "level": "Mittel",
            "steps": [
                "Laden Sie WinSetupFromUSB herunter, starten Sie das selbstextrahierende Archiv und wählen Sie die 64-Bit-Version (WinSetupFromUSB_x64.exe).",
                "Stecken Sie den USB-Stick an und wählen Sie ihn im Feld <em>USB disk selection</em> aus.",
                "Aktivieren Sie <em>Auto format it with FBinst</em> (wählen Sie FAT32; für ISO-Dateien über 4 GB NTFS, dann funktioniert aber nur der BIOS-/Legacy-Modus).",
                "Aktivieren Sie den Bereich des hinzuzufügenden Systems (z. B. <em>Vista/7/8/10/11/Server</em>) und wählen Sie die ISO-Datei über die Schaltfläche <em>…</em>. Für Linux nutzen Sie den Bereich <em>Linux ISO/Other Grub4dos compatible ISO</em>.",
                "Klicken Sie auf <em>GO</em> und bestätigen Sie die Warnungen. Warten Sie auf die Meldung <em>Job done</em>.",
                "Weitere Systeme fügen Sie hinzu, indem Sie das Programm erneut starten – diesmal <b>ohne</b> die Formatierungsoption.",
                "Testen Sie den Stick im QEMU-Emulator (Option <em>Test in QEMU</em>) oder starten Sie einen Rechner davon.",
            ],
        },
        "rufus": {
            "difficulty": "Einfach",
            "description": "Obwohl Rufus hauptsächlich für ein einzelnes System gedacht ist, lässt es sich als Grundlage für fortgeschrittenere Methoden verwenden.",
            "pros": ["Zuverlässig", "Schnell"],
            "cons": ["Keine native Multiboot-Unterstützung"],
            "platform": "Windows",
            "use": "USB-Stick mit einem einzelnen System",
            "level": "Niedrig",
            "steps": [
                "Laden Sie Rufus herunter (die portable Version benötigt keine Installation) und starten Sie es.",
                "Stecken Sie den USB-Stick an – er wird im Feld <em>Laufwerk</em> automatisch erkannt (ein Backup ist Pflicht, der Stick wird gelöscht).",
                "Klicken Sie auf <em>AUSWAHL</em> und wählen Sie die ISO-Datei des Systems.",
                "Wählen Sie das Partitionsschema: <em>GPT</em> für UEFI oder <em>MBR</em> für BIOS/Legacy (Rufus schlägt einen Wert für das jeweilige Image vor).",
                "Klicken Sie auf <em>START</em>, wählen Sie bei Nachfrage den ISO-Image-Modus und bestätigen Sie.",
                "Starten Sie den Rechner vom USB-Stick. Für Multiboot können Sie so einen Stick mit einem System erstellen oder stattdessen Ventoy verwenden.",
            ],
        },
    },
}


def get_methods(lang):
    """Łączy dane wspólne z tekstami w wybranym języku."""
    labels = LINK_LABELS[lang]
    methods = []
    for base in METHODS:
        method = {"id": base["id"], "name": base["name"]}
        method.update(CONTENT[lang][base["id"]])
        method["links"] = [
            {
                "label": labels[link["key"]],
                "url": link["url"].format(lang=lang),
                "primary": link.get("primary", False),
            }
            for link in base["links"]
        ]
        methods.append(method)
    return methods
