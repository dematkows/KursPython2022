# 4. Utwórz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia
# wiersz × kolumna.
table = [[0] * 10] * 10


for row in table:
    for col in row:
        print(col, end=" ")
    print()

# for i in range()
