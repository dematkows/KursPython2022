# 3. W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

chain = input("Give me some char chain: ")
lower_chars = 0
upper_chars = 0
digits = 0
others = 0

for char in chain:
    if char.islower():
        lower_chars += 1
    elif char.isupper():
        upper_chars += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print(f"Lower letters = {lower_chars}")
print(f"Upper letters = {upper_chars}")
print(f"Digits = {digits}")
print(f"Others = {others}")
