# 2. Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy po kolei dodać. Poza pętlą
# umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
ingredients = ["pasta", "garlic", "meatballs", "tomatoes", "cheese", "olive oil", "italian spices"]
print("Prepare a frying pan and the following ingredients", ingredients)

sorted_ingredients = ["olive oil", "garlic", "meatballs", "tomatoes", "italian spices", "pasta"]
print("When the pan is hot, do the following:")
for ingredient in sorted_ingredients:
    print("Add", ingredient + '.')
print("It's most recommended to serve hot.")
print("Add some Grana Padano cheese on it, if you like.")
