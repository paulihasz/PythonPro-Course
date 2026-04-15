name = "Alice"
age = 30
grades = [5, 4, 5, 6, 5]
is_student = True
average = sum(grades)/len(grades)

student = {
"imie": name,
"wiek": age,    
"srednia": average,
"czy_student": is_student,
"oceny": grades
}

# def opisz_zmienna(zmienna):
#     return f"{zmienna}[{zmienna.__class__}]"

# for zmienna in (name, age, average, is_student):
#     print(opisz_zmienna(zmienna))

for key, value in student.items():
    print(key, ":", value)


# print(type(name))      # Output: <class 'str'>
# print(type(age))       # Output: <class 'int'>
# print(type(average))   # Output: <class 'float'>
# print(type(is_student)) # Output: <class 'bool'>

