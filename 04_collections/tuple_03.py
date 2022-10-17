# 3. Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na
# krotce wyświetl jej indeks.

my_tuple = (1, 2, 3, 4)
user_number = int(input("Podaj liczbę: "))

# 1.
for index in range(len(my_tuple)):
    if my_tuple[index] == user_number:
        print("Indeks trafionej krotki:", index)
    else:
        pass
print()

# 2.
for index, value in enumerate(my_tuple):
    if value == user_number:
        print("Indeks trafionej krotki:", index)
    else:
        pass
print()

# 3.
print(f"Is number {user_number} in tuple: {user_number in my_tuple}")
print(f"Number {user_number} is on index {my_tuple.index(user_number)}")
