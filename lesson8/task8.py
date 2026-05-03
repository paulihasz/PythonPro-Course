#Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError , przekazując do niego tę listę.

class BladWalidacjiError(Exception):
    ...


def walidacja_hasla(haslo: str):
    
    err_lst = []
    
    if len(haslo) < 8:
        err_lst.append('hasło za krótkie')
    
    if not any(znak.isupper() for znak in haslo):
        err_lst.append('brak wielkiej litery')
        
    if not any(znak.isdigit() for znak in haslo):
        err_lst.append('brak cyfry w haśle')
        
    if any(znak.isalnum() for znak in haslo):
        err_lst.append('brak znaku specjalnego')
        
    if err_lst:
        raise BladWalidacjiError(*err_lst)
        
        
        
try:
    walidacja_hasla('haslo1q')
except BladWalidacjiError as e:
    bledy = e
    print(f"błędy {e}")
    