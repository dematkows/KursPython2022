user_value = input("Podaj liczbę od 1 do 100: ")

if user_value.isdigit():
    user_value = int(user_value)
else:
    ValueError()

number = user_value / 4
print(f" Number = { number }")
