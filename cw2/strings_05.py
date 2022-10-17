# 5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały
# bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
text = input("Give a sentence to check palindrome: ")

text = text.replace(" ", "")
text = text.lower()
print('Is palindrome?:', text == text[::-1])
