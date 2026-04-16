# Gra "Zgadnij liczbę":
# Program "myśli" o liczbie (np. sekret = 42 ).
# Użyj pętli while True , aby w nieskończoność prosić użytkownika o podanie liczby.
# Wewnątrz pętli, sprawdź, czy podana liczba jest równa sekretnej. Jeśli tak, wyświetl
# gratulacje i użyj break , aby zakończyć grę. Jeśli nie, poinformuj, że to zła liczba.

secret_number = 42

while True:
    shot = int(input('Guess the number: '))
    if shot == secret_number:
        print('Congratulations!')
        break #zakończenie pętli
    else:
        print('Wrong number, try again')

