# 4. Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

elements = []
list_size = int(input("How many elements do you want to provide? (only even numbers are acceptable): "))
if list_size % 2 == 0:
    pass
else:
    print("You provided an odd number!")
    exit(1)

for e in range(list_size):
    print("Give an element no.", e + 1, ": ", end='')
    element = input()
    elements.append(element)

element1 = elements[(len(elements) - 1) // 2]
element2 = elements[((len(elements) - 1) // 2) + 1]
comparison = element1 == element2

print("\nAre the two central elements of the list the same?: ", comparison)
