# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech
# środkowych znaków danego ciągu.
txt = 'ABRACADABRA'
print("", txt)
txt_length = len(txt)
index_center = txt_length // 2
index_prev = index_center - 1
index_next = index_center + 1

# 1.
print("", txt[index_prev] + txt[index_center] + txt[index_next])

# 2.
print("", txt[index_prev:index_next + 1])
