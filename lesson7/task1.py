# #Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka", "truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te słowa, które mają więcej niż 5 liter

words = ['apple', 'banana', 'kiwi', 'pear', 'strawberry']

filtered_words = [word for word in words if len(word) > 5]
print(filtered_words)

print(list(filter(lambda x: len(x) > 5, words)))