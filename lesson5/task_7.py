# Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue , aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in "aeiouy": continue ).

sentence = input('Napisz dowolne zdanie: ')
vowels = 'aeiouyAEIOUY'
sentence_vowels = 0

for letter in sentence:
    if letter in vowels:
        sentence_vowels += 1
        print(letter)
        
print(f'Number of vowels in this sentence: {sentence_vowels}') 

