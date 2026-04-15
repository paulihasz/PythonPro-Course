# Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo "Python" na liczbę całkowitą. Uruchom go, zobacz błąd ValueError , a następnie "napraw" program, umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego kod nie działał.

word = 'Python'
word_int = int(word) # nie można przekonwertować ciągu znaków  niezawierajcych liczb na integer|float

print(word_int)


# zad. 8__________________________________________________________

dogs_age = int(input('Podaj wiek twojego psa: '))

if dogs_age == 1:
    human_age = 15
elif dogs_age == 2:
    human_age = 15 + 9
else:
    human_age = 15 + 9 + (dogs_age - 2) * 5

print(f'Wiek psa w latach ludzkich: {human_age}')

# zad 9 Identyfikator po zmianie: Utwórz zmienną x = 10, wyświetl jej id(), następnie przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się zmienił? Dlaczego? Odpowiedz w komentarzu.

x = 10

print(id(x))

x = x + 1

print(id(x))