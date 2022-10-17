# Testy1
my_list = ["Ada", "Ruby", "Julia", "Violet"]

length = len(my_list)
for index in range(length):
    print(index, ":", my_list[index])

# Testy2
pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)
