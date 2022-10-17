# 4.Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
print("\n4.Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:")
title = input('Podaj tytuł książki: ')
author_surname = input('Podaj nazwisko autora: ')
pages = input('Podaj liczbę stron: ')

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print("\na. Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.")
print('Is the title only alphabetic?:', title.replace(' ', '').isalpha())
print('Is the author surname only alphabetic?:', author_surname.isalpha())
print('Is the pages value a digit?:', pages.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print("\nb. Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich.")
title = title.title()
author_surname = author_surname.capitalize()
print("Title:", title)
print("Author Surname:", author_surname)

# Połącz dane w jeden ciąg book za pomocą spacji
print("\nc. Połącz dane w jeden ciąg book za pomocą spacji.")
book = title + " " + author_surname
print("book =", book)

# Policz liczbę wszystkich znaków w napisie book
print("\nd. Policz liczbę wszystkich znaków w napisie book.")
print("", book.count(''))
print("", len(book))
