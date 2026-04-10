# 1 opowieść o sobie:
name = input('podaj imię: ')
hobby = input('podaj hobby: ')
cel = input('podaj cel: ')
print(f'Nazywam się {name}. Moim hobby jest {hobby}. Moim celem jest {cel}.')

# interaktywny dialog
imie = input('podaj imię: ')
wiek = input('podaj wiek: ')    
miasto = input('podaj miasto: ')
print(f'Nazywam się {imie}. Mam {wiek} lat. Mieszkam w {miasto}.')

# kalkulator obwodu
length = float(input('podaj długość: '))
width = float(input('podaj szerokość: '))
perimeter = 2 * (length + width)
print(f'Obwód prostokąta o długości {length} i szerokości {width} wynosi {perimeter}.')

# kreator postaci
race = input('podaj rasę: ')
character_class = input('podaj klasę: ')
print(f'stworzono postać rasy {race} i klasy {character_class}.')

# wyrażenie logiczne
age = int(input('podaj wiek: '))
has_license = input('czy masz prawo jazdy? (tak/nie): ')
if age >= 18 and has_license == 'tak':
    print('Możesz prowadzić samochód.')
else:
    print('Nie możesz prowadzić samochodu.')
    
# konwerter temp
celsius = float(input('podaj temperaturę w stopniach Celsjusza: '))
fahrenheit = (celsius * 9/5) + 32
print(f'{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.')