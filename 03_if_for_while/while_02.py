# 2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
user_num = 0
while user_num != secret_num:
    user_num = int(input("Guess the secret number [0-20]: "))
print("Congratz! It was", secret_num)
