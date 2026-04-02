user_number1 = float(input('Enter the first number: '))
user_number2 = float(input('Enter the second number: '))
operation = input('Enter the operation (+, -, *, /): ')

if operation == '+':
    result = user_number1 + user_number2
    print(f'The result of adding {user_number1} and {user_number2} is: {result}')
elif operation == '-':
    result = user_number1 - user_number2
    print(f'The result of subtracting {user_number2} from {user_number1} is: {result}')
elif operation == '*':
    result = user_number1 * user_number2
    print(f'The result of multiplying {user_number1} and {user_number2} is: {result}')
elif operation == '/':
    if user_number2 != 0:
        result = user_number1 / user_number2
        print(f'The result of dividing {user_number1} by {user_number2} is: {result}')
    else:
        print('Error: Division by zero is not allowed.')    
    