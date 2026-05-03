# def name_test(name):
#     assert len(name) > 3
    
# name_test('1')

#Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta.

def oblicz_srednia(lista_ocen):
    assert len(lista_ocen) > 0, "Lista ocen nie może być pusta"
    return sum(lista_ocen) / len(lista_ocen)

oblicz_srednia([])

