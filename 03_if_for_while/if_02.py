# 2. Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

number1 = int(input("Give the first whole number: "))
number2 = int(input("Give the second whole number: "))

result = number1 + number2

if result > 100:
    print("The sum of both numbers:", result)
else:
    print("The end.")
