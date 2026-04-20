def password_checker(password: str) -> bool:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any (i.isdigit() for i in password):
        print("Password must contain at least one digit.")
        return False
    if not any (i.isupper() for i in password):
        print("Password must contain at least one uppercase letter.")
        return False
    return True

        


while True:
    user_password = input("Enter your password: ")
    if password_checker(user_password):
        print("Password is valid.")
        break   
    else:
        answer = input("Try again: Y / Stop: N ").upper()
    if answer == 'N':
        break

