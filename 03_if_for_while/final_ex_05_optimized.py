# 5. Stwórz grę ciepło-zimno.

import random

user_pick_previous = -100
distance = 0
# Komputer losuje liczbę z zakresu od 1 do 100.
ai_number_pick = random.randrange(1, 101)
# ===== Poniższa linijka do potrzeb testowych =====
print("AI wybrało:", ai_number_pick)

for i in range(0, 6):
    # Użytkownik podaje swój traf.
    user_pick_next = int(input("Podaj swój traf [1-100]: "))
    # Jeśli użytkownik zgadnie wygrywa gracz.
    if user_pick_next == ai_number_pick:
        print("Użytkownik wygrał!\nTrafiona liczba to:", ai_number_pick)
        exit(0)
    else:
        pass
    distance = abs(user_pick_next - ai_number_pick)
    distance_prev = abs(user_pick_previous - ai_number_pick)

    # Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
    if distance <= distance_prev:
        print("+++ ciepło +++")
        print("Pozostała liczba prób:", 6 - i)
        # ===== Poniższa linijka do potrzeb testowych =====
        print("Teraz:", distance, "Wczesniej:", distance_prev, '\n')
    else:
        print("--- zimno ---")
        print("Pozostała liczba prób:", 6 - i)
        # ===== Poniższa linijka do potrzeb testowych =====
        print("Teraz:", distance, "Wczesniej:", distance_prev, '\n')
    user_pick_previous = user_pick_next
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
print("\nKomputer wygrał!\nLiczba wybrana przez AI to:", ai_number_pick)
