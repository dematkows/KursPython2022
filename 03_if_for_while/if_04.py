# 4. Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy
# zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

string1 = "Abr@kadabra4"

if len(string1) > 5 and 'a' in string1:
    print(string1.replace('a', 'z'))
else:
    pass
