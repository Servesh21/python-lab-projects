sent = input("Enter a sentence: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_symbols = 0

for i in sent:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        if i in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
    elif i == " ":
        spaces += 1
    else:
        special_symbols += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special symbols: {special_symbols}")
