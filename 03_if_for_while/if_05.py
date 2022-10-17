# 5. Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i
# mieć długość conajmniej 8 znaków i nie więcej niż 24 znaki. Poinformuj użytkownika, jeśli wpisane hasło jest nie
# poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = str(input("Input the password: "))

if len(password) < 8:
    print("Password too short (less than 8 characters)!")
elif len(password) > 24:
    print("Password too long (more than 24 characters)!")
elif password.isdigit():
    print("Password should contain alphabet")
elif password.isalpha():
    print("Password should contain at least 1 digit")
elif password.islower():
    print("Password is all lowercase - it should contain an uppercase also")
elif password.isupper():
    print("Password is all uppercase - it should contain a lowercase also")
else:
    print("Password is strong.")
