height = float(input('Enter your height in centimeters: '))
parent = input('Do you have parental guidance? (yes/no): ').strip().lower()
if height >= 120 and parent == 'yes':
    print('You are tall enough to access the attraction.')
elif height >= 160:
    print('You are tall enough to access the attraction without parental guidance.')
else:
    print('You are not tall enough to access the attraction.')