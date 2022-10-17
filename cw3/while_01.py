# 1. Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celsjuszach. Program powinien wykonać się w
# pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

# For style
f_degree = 0
c_degree = 0
for f_degree in range(0, 201, 20):
    c_degree = 5 / 9 * (f_degree - 32)
    c_degree = round(c_degree, 2)
    print(f"{f_degree} st F -> {c_degree} st C")

print()

# While style
f_degree = 0
c_degree = 0
while f_degree <= 200:
    c_degree = 5 / 9 * (f_degree - 32)
    c_degree = round(c_degree, 2)
    print(f"{f_degree} st F -> {c_degree} st C")
    f_degree += 20
