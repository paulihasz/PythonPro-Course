# 1 input...
def wczytaj_plik():
    sciezka = input('podaj sciezke do pliku: ')
    try:
        plik = open(sciezka, mode='r')
        print('ok')
    except FileNotFoundError:
        print(f'plik o nazwie {sciezka} nie istnieje')
    except PermissionError:
        print(f'brak dostepu do pliku {sciezka}')
    else:
        plik.close()    
        
wczytaj_plik()


