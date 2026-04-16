# Mini-projekt: Prosty kalkulator walut:
# Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3}W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
# Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
# Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
# Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break .


rates = {"USD": 4.0, 
         "EUR": 4.3}

while True:
    pln = float(input("enter amount in PLN: "))
    currency = input("enter currency: USD / EUR ").upper()

    if currency in rates:
        final = pln / rates[currency]
        print(f"The exchange of {pln:.2f} PLN is {final:.2f} {currency}")
    else:
        print("You entered an invalid currency!")
        
    if input("Do you want to continue? Enter 'yes' or 'no'") == 'no':
        break