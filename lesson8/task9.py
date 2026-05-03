# Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania pliku.

def czytaj_plik():
    
    try:
        with open("out.txt", "r", encoding="utf-8") as file:
            zawartosc = file.read()
            print("Zawartość piku:")
            print(zawartosc)
    
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje.")

    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu pliku.")
        
czytaj_plik()