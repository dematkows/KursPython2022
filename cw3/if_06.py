# 6. Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl
# komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

guess_var = 8
user_var = int(input("Guess the secret number [in range of 1-100]: "))

if user_var == guess_var:
    print("Gratulacje! To była liczba", guess_var)
else:
    print("Pudło!")
