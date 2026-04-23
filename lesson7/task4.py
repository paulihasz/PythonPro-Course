# Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać # tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która # sprawdza, czy liczba jest pierwsza)

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

# Stwórz listę liczb od 1 do 30
liczby = list(range(1, 31))

# Użyj filter() do znalezienia liczb pierwszych
liczby_pierwsze = list(filter(czy_pierwsza, liczby))
print("Liczby pierwsze od 1 do 30:", liczby_pierwsze)   

