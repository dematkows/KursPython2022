# 8. Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.

# If style:
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
number3 = int(input("Give the third number: "))

if number1 >= number2 >= number3:
    print("The maximum number is:", number1)
    print(str(number1) + ',', str(number2) + ',', str(number3))
elif number2 >= number1 >= number3:
    print("The maximum number is:", number2)
    print(str(number2) + ',', str(number1) + ',', str(number3))
elif number1 >= number3 >= number2:
    print("The maximum number is:", number1)
    print(str(number1) + ',', str(number3) + ',', str(number2))
elif number2 >= number3 >= number1:
    print("The maximum number is:", number2)
    print(str(number2) + ',', str(number3) + ',', str(number1))
elif number3 >= number2 >= number1:
    print("The maximum number is:", number3)
    print(str(number3) + ',', str(number2) + ',', str(number1))
else:
    print("The maximum number is:", number3)
    print(str(number3) + ',', str(number1) + ',', str(number2))

# Sort style
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
number3 = int(input("Give the third number: "))
numbers = [number1, number2, number3]
sorted_numbers = sorted(numbers, key=None, reverse=True)
print("The maximum number is:", sorted_numbers[0])
print(sorted_numbers)
