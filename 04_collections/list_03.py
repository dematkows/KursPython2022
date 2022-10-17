# 3. Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

# The lazy style
numlist = input("Podaj listę liczb oddzielonych spacją: ")
numlist.split(' ')
print(f"Czy pierwszy i ostatni element są takie same?: {numlist[0] == numlist[-1]}\n")

# The spectacular style
numlist = []
for n in range(5):
    num = int(input("Podaj jedną liczbę: "))
    numlist.append(num)

if numlist[0] == numlist[-1]:
    print("Pierwszy i ostatni element są takie same.")
else:
    print("Pierwszy i ostatni element nie są takie same.")
