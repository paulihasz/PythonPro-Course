# Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50% zniżki. Użyj operatorów or i and .

cash = 100
student = input('Are you a student? Y/N: ')
age = int(input('How old are you? '))

if student == 'Y'.lower() or age < 18:
    print(f'You are eligible for a 50% discount: {cash * 0.5} PLN')
else:
    print('You are not eligible for a discount.')
