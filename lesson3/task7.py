value = bool(int(input('Wybierz wartość: 0 lub 1 ')))
value_2 = bool(int(input('Wybierz wartość: 0 lub 1 ')))

value_3 = value and value_2
value_4 = value or value_2

def get_boolean(idx: int):
    while True:
        resp = int(f'{idx} Wybierz wartość: 0 lub 1 ')
        if resp in {'1', '0'}:
            return bool(int(resp))
        print('niepoprawna cyfra')
        
bool0 = get_boolean(1)
bool1 = get_boolean(2)        
        
print(value_3)
print(value_4)