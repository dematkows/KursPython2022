# 4. Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]

list0 = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

for x in range(0, len(list0), len(list0)//3):
    xlist = list0[x:x+(len(list0)//3)]
    xlist.reverse()
    print(xlist)
