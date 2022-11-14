# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
# atrybuty: imię, kolor sierści, rasę
# metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog:
    def __init__(self, name, fur_color, race):
        self.name = name
        self.fur_color = fur_color
        self.race = race

    def bark(self):
        return 'Woof!'

    def tail_wag(self, number):
        return '*Mach ' * number


pixie = Dog("Pixie", "black & white", "border collie")
dixie = Dog("Dixie", "yellow", "labrador")
dust = Dog("Dust", "grey", "unknown")
lassie = Dog("Lassie", "white", "lassie")

print(pixie.name)
print(pixie.bark())
print(pixie.tail_wag(4))
