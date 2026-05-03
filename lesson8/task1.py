while True:
    try:
        fnum = float(input('podaj liczbę: '))
        snum = float(input('podaj drugą liczbę: '))
        dzialanie = input('podaj działanie: ')
        func_dict = {"+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                    "/": lambda x, y: x / y}
        result = func_dict[dzialanie](fnum, snum)
    except ValueError as e:
        print("to nie jest liczba", e.args[0].split(' ')[-1])
    except KeyError:
        print("niepoprawne działanie")
    except ZeroDivisionError:
        print("niepoprawne działanie dzielenia przez 0")
    else: # wykona się jeśli nie było błędu
        print(f'wynik: {result}')
        break
    finally:#wykona się zawsze po każdej pętli, nawet po błedzie
        print('Kolejna operacja...\n')
    