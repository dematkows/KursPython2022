# 3. Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

letters = ('a', 'b', 'b', 'b', 'c', 'd', 'd')
numbers = (1, 2, 3, 4, 4, 4, 5)

print(letters[::2])
print(numbers[1::2])

new_list = letters[::2] + numbers[1::2]
print(new_list)
print(set(new_list))
