# Analiza wieku: Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
# if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
# "Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+).

age = int(input('How old are you? '))

if age <= 1:
    print('You are an infant')
elif age <= 12:
    print('You are a child')
elif age <= 17:
    print('You are a teenager')
elif age <= 64:
    print('You are an adult')
else:
    print('You are a senior')
    



# tenary operator 

status = "Adult" if age >= 18 else "Minor"

print(status)