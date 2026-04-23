# Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
# jednej linijce.

numbers = [-5, 2, 8, -1, 0, 10]

filtered_numbers = [x * x for x in numbers if x > 0]

print(filtered_numbers)

filtred_numbers_map = list(map(lambda x: x * x, filter(lambda x: x > 0, numbers)))

print(filtred_numbers_map)