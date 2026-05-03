# Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej linii tekstu. Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec".


with open("dziennik.txt", encoding='utf8', mode='a') as f:
    
    while True:
        text = input("enter text: ")
        f.write(text + '\n')
        if text == 'stop':
            break

        
print("Tekst został zapisany do pliku dziennik.txt")
    
