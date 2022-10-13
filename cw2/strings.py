# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech
# środkowych znaków danego ciągu.
print("1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech "
      "środkowych znaków danego ciągu.")

txt = 'ABRACADABRA'
print("", txt)
txt_length = len(txt)
index_center = txt_length // 2
index_prev = index_center - 1
index_next = index_center + 1

print("", txt[index_prev] + txt[index_center] + txt[index_next])
print("", txt[index_prev:index_next + 1])


# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
print("\n2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku "
      "s1.")
s1 = "Fruit"
s2 = "Loops"
s1_center = len(s1) // 2
s3 = s1[:s1_center] + s2 + s1[s1_center:]

print("s1 = \"Fruit\"", "\ns2 = \"Loops\"", "\ns3 =", s3)


# 3. Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:
print("\n3. Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:")
quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
print("\na. Policz wszystkie znaki w napisie:\n", "", len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
print("\nb. Nie modyfikując zmiennej wyświetl słowo wisdom:\n", "", quote[-7:-1])

# Wyświetl tylko pierwszą połowę tekstu
quote_length = len(quote)
index_center = quote_length // 2
print("\nc. Wyświetl tylko pierwszą połowę tekstu:\n", "", quote[:index_center + 1])

# Wyświetl tylko kropkę
print("\nd. Wyświetl tylko kropkę:\n", "", quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print("\ne. Wyświetl od połowy tylko co trzecią literę cytatu:\n", "", quote[index_center + 1::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print("\nf. Wyświetl ‘Hnsyi h is hpe ntebo fwso.’:\n", "", quote[::2])

# Wyświetl cały cytat odwrotnie
print("\ng. Wyświetl cały cytat odwrotnie:\n", "", quote[::-1])

# Zamień wisdom na słowo friendship
print("\nh. Zamień wisdom na słowo friendship:\n", "", quote.replace('wisdom', 'friendship'))


# 4.Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
print("\n4.Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:")
title = input('Podaj tytuł książki: ')
author_surname = input('Podaj nazwisko autora: ')
pages = input('Podaj liczbę stron: ')

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print("\na. Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.")
print('Is the title only alphabetic?:', title.isalpha())
print('Is the author surname only alphabetic?:', author_surname.isalpha())
print('Is the pages value a digit?:', pages.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print("\nb. Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich.")
print("Title:", title.title())
print("Author Surname:", author_surname.capitalize())

# Połącz dane w jeden ciąg book za pomocą spacji
print("\nc. Połącz dane w jeden ciąg book za pomocą spacji.")
book = title + " " + author_surname
print("book =", book)

# Policz liczbę wszystkich znaków w napisie book
print("\nd. Policz liczbę wszystkich znaków w napisie book.")
print("", book.count(''))
print("", len(book))


# 5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały
# bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
print("\n5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma "
      "mały bok. \nPozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest "
      "palindromem.")
text = input("Give a sentence to check palindrome: ")

text = text.replace(" ", "")
text = text.lower()
print('Is palindrome?:', text == text[::-1])


# 6. Przekopiuj zawartość import this do zmiennej.
print("\n6. Przekopiuj zawartość import this do zmiennej.")

variable = "The Zen of Python, by Tim Peters" \
           "\nBeautiful is better than ugly." \
           "\nExplicit is better than implicit." \
           "\nSimple is better than complex." \
           "\nComplex is better than complicated." \
           "\nFlat is better than nested." \
           "\nSparse is better than dense." \
           "\nReadability counts." \
           "\nSpecial cases aren't special enough to break the rules." \
           "\nAlthough practicality beats purity." \
           "\nErrors should never pass silently." \
           "\nUnless explicitly silenced." \
           "\nIn the face of ambiguity, refuse the temptation to guess." \
           "\nThere should be one-- and preferably only one --obvious way to do it." \
           "\nAlthough that way may not be obvious at first unless you're Dutch." \
           "\nNow is better than never." \
           "\nAlthough never is often better than *right* now." \
           "\nIf the implementation is hard to explain, it's a bad idea." \
           "\nIf the implementation is easy to explain, it may be a good idea." \
           "\nNamespaces are one honking great idea -- let's do more of those!"

# Policz liczbę wystąpień słowa better.
print("\na. Policz liczbę wystąpień słowa better.")
print("", variable.count("better"))

# Usuń z tekstu symbol gwiazdki
print("\nb. Usuń z tekstu symbol gwiazdki.")
print("After replacement:\n", variable.replace('*', ''))

# Zamień jedno wystąpienie explain na understand
print("\nc. Zamień jedno wystąpienie explain na understand.")
print("After replacement:\n", variable.replace('explain', 'understand', 1))

# Usuń spacje i połącz wszystkie słowa myślnikiem
print("\nd. Usuń spacje i połącz wszystkie słowa myślnikiem.")
print("After replacement:\n", variable.replace(' ', '-'))

# Podziel tekst na osobne zdania za pomocą kropki
print("\ne. Podziel tekst na osobne zdania za pomocą kropki.")
print("After splitting:\n", variable.split('.'))

# 7. Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(), by wyświetlić zdanie
# zawierające te wartości.
print("\n7. Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(), "
      "by wyświetlić zdanie zawierające te wartości.")
v1 = 1234
v2 = "abcd"
print("Numeric value is {} and alphabetic value is {}".format(v1, v2))
