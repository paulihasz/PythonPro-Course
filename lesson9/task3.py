# Konfiguracja w JSON: Stwórz słownik Pythona z ustawieniami aplikacji, np.
# konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc":
# [1920, 1080]} . Zapisz ten słownik do pliku config.json z wcięciami i poprawnym kodowaniem polskich znaków.

import json
CONFIG_FILE = "config.json"


konfiguracja = {
                "uzytkownik": "admin",
                "motyw": "ciemny",
                "rozdzielczosc": [1920, 1080]
                }

with open(CONFIG_FILE, "w", encoding="utf-8") as fp:
    json.dump(konfiguracja, fp)



