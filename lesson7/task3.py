# 3. Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion imiona =
# ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą.

imiona = ["anna", "piotr", "kasia"]

poprawione_imiona = list(map(lambda x: x.capitalize(), imiona))
print(poprawione_imiona)

names = [name.capitalize() for name in imiona]
print(names)