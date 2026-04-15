#zad 2
a, b, c = 256, 256, 256
print(id(a), id(b), id(c))

x, y, z = int("257"), int("257"), int("257")
print(id(x), id(y), id(z))


# zad 3
lst0 = [1, 1]
lst1 = [1, 1]
print("==", lst0 == lst1, "is", lst0 is lst1)