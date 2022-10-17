# 1. Na kartce papieru oblicz jak twój wiek będzie reprezentowany binarnie. Sprawdź, czy to samo zwróci Python.
age = int(input("Type your age [years]: "))
print("Your binary age is:", bin(age).lstrip('0b'))
