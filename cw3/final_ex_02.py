# 2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa
# sposoby - za pomocą pętli oraz przez string slicing ( ‘abrakadabra’ -> ‘baaar’).

# Loop style
text = input("Give me a text: ")
len_text = len(text)

for i in range(1, len_text, 2):
    print(text[i], end='')

# Slicing style
print("\n" + text[1::2])
