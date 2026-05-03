# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku finally , aby upewnić się, że plik z logami jest zawsze zamykany.

with open('log.txt', 'a', encoding='utf-8') as log_file:
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
            log_file.write(f"ValueError: {e}\n")
            print("to nie jest liczba", e.args[0].split(' ')[-1])
        except KeyError:
            log_file.write("KeyError: niepoprawne działanie\n")
            print("niepoprawne działanie")
        except ZeroDivisionError:
            log_file.write("ZeroDivisionError: niepoprawne działanie dzielenia przez 0\n")
            print("niepoprawne działanie dzielenia przez 0")
        else: # wykona się jeśli nie było błędu
            print(f'wynik: {result}')
            break
        finally:#wykona się zawsze po każdej pętli, nawet po błedzie
            print('Kolejna operacja...\n')
