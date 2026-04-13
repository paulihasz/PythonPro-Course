# kalkulator bmi

weight = float(input("Podaj swoją wagę w kilogramach: "))
height = float(input("Podaj swój wzrost w metrach: "))

bmi = weight / (height * height)
print(f"Twoje BMI to: {bmi:.2f}")

def f_c():...
def c_f():...

klucz = input('podaj wzór')
{'f_c': f_c,
 'c_f': c_f}[klucz]