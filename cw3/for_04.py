# 4. Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika,
# ale nie większe niż 8).

number = int(input("Give a number [0-8]: "))

if number not in range(0, 9):
    print("Błąd! (Wprowadzono liczbę spoza zakresu)")
else:
    print(str(number) + '! =', end=' ')
    result = 1

    if number > 1:
        for n in range(1, number + 1):
            result = n * result
            print(n, end=' ')
            if n != number:
                print('*', end=' ')
            else:
                continue
        print("=", result)
        print("Silnia z", number, "wynosi", result)
    else:
        print(result)
        print("Silnia z", number, "wynosi", result)
