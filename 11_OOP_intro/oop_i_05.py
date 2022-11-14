# Utwórz klasę sklep. Sklep posiada różne produkty. W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    def __init__(self, items: list) -> None:
        self.items = items

    def show_product(self, item_id):
        try:
            product, size = self.items[item_id]
            print(f"{item_id} - rozmiar {size}")
        except (IndexError, TypeError):
            print("Nie ma takiego produktu :(")

    def try_product(self, item_id, user_size):
        try:
            product, size = self.items[item_id]
            if size == user_size:
                print("Pasuje!")
            else:
                print("Nie pasuje :(")
        except (IndexError, TypeError):
            print("Nie ma takiego produktu")

    def buy_product(self, item_id):
        try:
            print(f"Kupujesz {self.items[item_id]}")
            self.items.pop(item_id)
        except (IndexError, TypeError):
            print("Nie ma takiego produktu")

    def return_product(self, product):
        if len(product) == 2:
            self.items.append(product)
        else:
            print("To nie jest produkt u nas kupiony")


product_list = Shop([
    ["T-Shirt", "M"],
    ["Trousers", "L"],
    ["Sneakers", "42"]
])

product_list.show_product(2)
product_list.try_product(2, 'XL')
product_list.buy_product(2)
print(product_list.items)
product_list.return_product(["Trousers", "L"])
print(product_list.items)
