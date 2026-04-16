# Odliczanie do startu: Użyj pętli while , aby stworzyć program odliczający od 10 do 1. Po odliczeniu, poza pętlą, program powinien wyświetlić "Start!".

number = 10

while number >= 0:
    print(number)
    number -= 1

print('start!')   

#_____________________________________________________________

for number in range(10, -1, -1): #od czego zaczynam, do jakiej liczby idziemy, o ile zmniejszamy
    print(number)

print('start!')

