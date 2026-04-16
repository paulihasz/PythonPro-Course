# Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr", "Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z instrukcją break oraz blokiem else , aby: Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę. Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
# liście."

list_of_names = ["Anna", "Jan", "Piotr", "Kasia"]
name = input('enter the name: ').title()

for x in list_of_names:
    if name == x:
        print('there is a name on the list')
        break
else:
        print('the entered name was not found on the list')

