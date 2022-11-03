# 1. Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinien się znaleźć w nowej linii. Utwórz funkcję,
# która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************
# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#
# plik z cytatami powinien również zawierać informację o autorze, wyświetl cytat i pod spodem autora
import random


def open_file():
    filename = input("Give me the name of the file (including extension): ")
    with open(filename) as file:
        return file.readlines()


def get_random_quote(list_of_quotes):
    return random.choice(list_of_quotes).strip()


def show(quote):
    print("Quote of the day is:\n")
    txt, author = quote.split(' -')
    print('*' * 100)
    print(txt.center(100))
    print(author.center(100))
    print('*' * 100)


def main():
    all_quotes = open_file()
    quote = get_random_quote(all_quotes)
    show(quote)


main()
