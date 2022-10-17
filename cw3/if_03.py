# 3. Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od
# wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna,
# 4 i mniej - nie warta uwagi.

opinion1 = int(input("What is your opinion1 about the book? [1-10]: "))
opinion2 = int(input("What is your opinion2 about the book? [1-10]: "))
opinion3 = int(input("What is your opinion3 about the book? [1-10]: "))

avg_opinion = (opinion1 + opinion2 + opinion3) / 3
print("The average opinion about the book is:", round(avg_opinion, 1))

if avg_opinion > 7:
    print("Mark: bardzo dobra")
elif avg_opinion >= 5:
    print("Mark: przecietna")
else:
    print("Mark: nie warta uwagi")
