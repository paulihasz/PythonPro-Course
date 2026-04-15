users_name = input("Podaj swoje imię: ")
users_birth_year = int(input("Podaj swój rok urodzenia: "))

users_age = 2026 - users_birth_year
print(f"Cześć, {users_name}! Masz {users_age} lat.")