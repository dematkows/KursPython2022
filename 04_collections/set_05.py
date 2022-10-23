# 5. Porównaj zachowanie discard() vs remove() dla typu set.

my_set = {'w', 'e', 'r', 't', 'q', 'y'}

print("The discard() method won't do anything if the specified item is not present in the set, whereas remove() "
      "method will raise a KeyError in that case.")
my_set.discard('a')
my_set.remove('a')
