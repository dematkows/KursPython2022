# Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do
# kolejki (put), wyjęcie elementu z kolejki (get). Utwórz kilka obiektów klasy Queue z różnymi parametrami.

class Queue:
    def __init__(self, list):
        self.list = list

    # def show_queue(self):
    #     print(self.list)

    def __str__(self):
        return f"LIST: {self.list}"

    def is_queue_empty(self):
        # return True if len(self.list) == 0 else False
        return len(self.list) == 0

    def put_to_queue(self, element):
        self.list.append(element)
        print(f"Dodano element {element}!")

    def get_from_queue(self):
        return self.list.pop(0)


queue = Queue([3, 5, 6, 6, 7])

print(queue.list)
print(queue.is_queue_empty())
queue.put_to_queue(0)
print(queue)
print(queue.get_from_queue())
print(queue)
