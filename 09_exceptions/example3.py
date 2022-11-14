def open_file(filename):
    while True:
        try:
            with open(filename) as file:
                return file.read()
        except FileNotFoundError:
            print("Nie znaleziono takiego pliku.")
            filename = input("Podaj nazwę pliku: ")


namefile = "test.txt"
content = open_file(namefile)
print(content)
