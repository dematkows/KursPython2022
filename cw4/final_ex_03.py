# 1. Utwórz dowolną tablicę n x n zawierającą dowolny znak,
# a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją
# wejście:
# n = 3
# tab = [['-', '-', '-']
#   ['-', '-', '-'],
#   ['-', '-', '-']]
# wyjście:
# - - -
# - - -
# - - -

lista = [['-'] * 3] * 3
print(lista)
print()

for row in lista:
    print(row)
print()

# 1.
for row in lista:
    print(' '.join(row))
print()

# 2.
for row in lista:
    for col in row:
        print(col, end=" ")
    print()
