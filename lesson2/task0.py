# zapytaj o imie, wiek, miasto w pętli
# przechowaj odp. w slowniku
# wypelnij danymi ze slowanika
# pętle pyta o dane, kolejno


def pobierz_uzytkownika() -> dict:
    dane_uzytkownika = {} # klucz: wartość

    for informacja in ('name', 'age', 'city'):
        dane_uzytkownika[informacja] = input('wprowadź ' + informacja + ': ')
        
    return dane_uzytkownika

# pytamy o ilość uzytkownikow do wprowadzenia
# w pętli pytamy o kolejnych uzytkowników
# słowniki są przechowane w liście
        
# stworz pustą listę
# pobierz uzytkownikow
# pętla for iteruje po range

    
def pobierz_n_uzytkownikow(ilosc_uzytkownikow):
    users = []
    for _ in range(ilosc_uzytkownikow):
        user = pobierz_uzytkownika()
        users.append(user)
    return users    
        
liczba_uzytkownikow = int(input('podaj liczbę uzytkownikow: '))
if liczba_uzytkownikow <= 0:
    print('liczba musi być dodatnia')
else:
    users = pobierz_n_uzytkownikow(liczba_uzytkownikow)
    
    # while liczba_uzytkownikow != 0:
    #     user = pobierz_uzytkownika()
    #     users.append(user)
    #     liczba_uzytkownikow -= 1    
    
    # while len(users) < 3:
    #     user = pobierz_uzytkownika()
    #     users.append(user)
    
   
        