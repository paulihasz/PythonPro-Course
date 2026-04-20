def silnia(n):
    if n == 0 or n == 1:
        return 1
    return n * silnia(n - 1)

n = int(input("Podaj liczbę n: "))
print(f"{n}! = {silnia(n)}")