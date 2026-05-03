#Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik, klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except

# KeyError .
# dict_ = {'a': 1,
#         'b': 2}

# print(dict_.get('a'))


def pobierz_wartosc(slownik: dict, klucz):
    return slownik.get(klucz)


def pobierz_wartosc_try(slownik: dict, klucz):
    try:
        return slownik[klucz] #keyerror
    except KeyError:
        return None
    
    
