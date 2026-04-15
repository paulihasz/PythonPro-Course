# Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.

def oblicz_pole_prostokata(a: int | float, b:int | float) -> int | float:

    """funkcja przyjmuje wartości a oraz b i oblicza pole"""

#obliczam pole prostokąta
    pole = a * b
# pole obliczone

    return pole
bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")

print(oblicz_pole_prostokata(10, 50))