# 3. Stwórz listę 10 elementową (różne typy!). Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod
# indexem wybranym przez użytkownika. Obsłuż błędy.
items = [13, 'string', 2.45, False, [], (), {}, 200, 'lala', True]

try:
    index = int(input("Podaj index: "))
    user_item = items[index]
    x = 1 / user_item
    print("Wynik dzielenia: ", x)
except ValueError:
    print("Błędna wartość.")
except TypeError:
    print("Błąd typu.")
except ZeroDivisionError:
    print("Nie dziel przez zero.")
except IndexError:
    print("Wyszlismy poza zakres tablicy.")
