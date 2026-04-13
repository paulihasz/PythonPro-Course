value = bool(int(input('Wybierz wartość: 0 lub 1 ')))
value_2 = bool(int(input('Wybierz wartość: 0 lub 1 ')))

value_3 = value and value_2
value_4 = value or value_2

print(value_3)
print(value_4)