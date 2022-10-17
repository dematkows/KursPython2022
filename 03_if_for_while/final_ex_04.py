# 4. Napisz grę - kamień (k) / papier (p) / nożyce (n).
import random

figures = ['k', 'p', 'n']
wynik_user = 0
wynik_ai = 0
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
rounds = (input("Podaj liczbę rund: "))

# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
if rounds == 'koniec':
    exit(0)

for n in range(int(rounds)):
    # Użytkownik podaje jedną z 3 figur.
    user_figure = str(input("Wybierz - kamień (k) / papier (p) / nożyce (n): "))
    # Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
    if user_figure == 'koniec':
        break
    else:
        pass

    # Komputer losuje jedną z 3 figur.
    ai_figure = random.choice(figures)
    print("Komputer wybrał:", ai_figure)

    # Sprawdź kto wygrał tę rundę.
    if (user_figure == 'k' and ai_figure == 'k') \
            or (user_figure == 'p' and ai_figure == 'p') \
            or (user_figure == 'n' and ai_figure == 'n'):
        print("Runda", str(n + 1) + ':', "Remis")
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        print("=== Użytkownik " + str(wynik_user) + ':' + str(wynik_ai) + " Komputer ===\n")
    elif (user_figure == 'k' and ai_figure == 'n') \
            or (user_figure == 'p' and ai_figure == 'k') \
            or (user_figure == 'n' and ai_figure == 'p'):
        wynik_user += 1
        print("Runda", str(n + 1) + ':', "Użytkownik wygrał!")
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        print("=== Użytkownik " + str(wynik_user) + ':' + str(wynik_ai) + " Komputer ===\n")
    else:
        wynik_ai += 1
        print("Runda", str(n + 1) + ':', "Komputer wygrał!")
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        print("=== Użytkownik " + str(wynik_user) + ':' + str(wynik_ai) + " Komputer ===\n")

if wynik_user > wynik_ai:
    print("\n!!! Grę wygrał użytkownik " + str(wynik_user) + ':' + str(wynik_ai) + " !!!")
elif wynik_ai > wynik_user:
    print("\n!!! Grę wygrał komputer " + str(wynik_ai) + ':' + str(wynik_user) + " !!!")
else:
    print("\n!!! Remis  " + str(wynik_user) + ':' + str(wynik_ai) + " !!!")
