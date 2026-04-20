def calculator(num1, operator, num2):

            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return None
                return num1 / num2
            else:
                print("Invalid operator. Please try again.")
            
result = calculator(5, '+', 3)
if result is not None:
    print("Result:", result)
   