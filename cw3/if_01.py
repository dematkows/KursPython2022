# 1. Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty
# i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input("Give a number: "))
if number % 3 == 0:
    print("Your number is divide'able by 3")
else:
    print("Your number is not divide'able by 3")
