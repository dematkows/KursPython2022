# 2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

numbers = []

for n in range(0, 10):
    print("Podaj liczbę", n + 1, ": ", end='')
    number = int(input())
    numbers.append(number)

print("Nieparzyste liczby: ", end='')
for num in numbers:
    if num % 2 != 0:
        print(num, end=' ')
    else:
        pass
