# Odczyt konfiguracji: Napisz program, który odczytuje plik config.json z poprzedniego zadania i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].

import json
CONFIG_FILE = "config.json"

with open(CONFIG_FILE, encoding='utf8') as fp:
    wczytaj_konf = json.load(fp)
print(f'Witaj, {wczytaj_konf['uzytkownik']}! Twój motyw to {wczytaj_konf['motyw']}')