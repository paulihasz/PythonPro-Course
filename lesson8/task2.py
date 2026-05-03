class NiepoprawnyWiekError(Exception):
    pass

def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise NiepoprawnyWiekError(f"Użytkownik musi mieć co najmniej 18 lat {18 - wiek}", -1)
    print("Rejestracja zakończona sukcesem!")
 
 
 
    
try: #spróbuj to wykonać
    wiek_podany = int(input("Podaj swój wiek: "))
    rejestruj_uzytkownika(wiek_podany)

except NiepoprawnyWiekError as e:
    print('Użytkownik musi mieć co najmniej 18 lat, kod błędu:', e.args[1])
    
except ValueError:
    print("Wiek musi być liczbą!")
        