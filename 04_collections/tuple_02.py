# 2. Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

my_tuple = ('cat', 4, 'dog', 81, 'hamster', 'cat', 4)
# I'm creating a set from my_tuple to use it in the for loop, so repeated tuple elements are not iterated and printed
# twice.
my_tuple_unique = set(my_tuple)

print("Repeated tuple elements: ", end='')
for t in my_tuple_unique:
    my_tuple.count(t)
    if my_tuple.count(t) >= 2:
        print(t, end=', ')
    else:
        pass

# Note: I could also create a list with unique elements from tuple using for & if instead of set,
# but that would be too much work :)
