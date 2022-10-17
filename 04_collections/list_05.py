# 5. Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach
# będzie znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika .

# 1.
people = [
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]
print(people[0:1])
print(people[1:2])
print(people[2:3])
print(people[3:4])
print()

# 2.
for row in people:
    print(row)
print()

# 3.
for row in people:
    print(", ".join(row))
print()

# 4.
for row in people:
    print(row[0], row[1], "-", row[2])
print()

# 5.
for row in people:
    for col in row:
        print(col, end="----")
    print()
print()

# 6.
for row in people:
    for col in row:
        if col == row[-1]:
            print("-", col)
        else:
            print(col, end=" ")
print()
