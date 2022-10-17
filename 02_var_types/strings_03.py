# 3. Do zmiennej quote przypisz zdanie:
# „Honesty is the first chapter in the book of wisdom.”, a następnie:
print("\n3. Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”, a następnie:")
quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
print("\na. Policz wszystkie znaki w napisie:\n", "", len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
print("\nb. Nie modyfikując zmiennej wyświetl słowo wisdom:\n", "", quote[-7:-1])

# Wyświetl tylko pierwszą połowę tekstu
quote_length = len(quote)
index_center = quote_length // 2
print("\nc. Wyświetl tylko pierwszą połowę tekstu:\n", "", quote[:index_center + 1])

# Wyświetl tylko kropkę
print("\nd. Wyświetl tylko kropkę:\n", "", quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print("\ne. Wyświetl od połowy tylko co trzecią literę cytatu:\n", "", quote[index_center + 1::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print("\nf. Wyświetl ‘Hnsyi h is hpe ntebo fwso.’:\n", "", quote[::2])

# Wyświetl cały cytat odwrotnie
print("\ng. Wyświetl cały cytat odwrotnie:\n", "", quote[::-1])

# Zamień wisdom na słowo friendship
print("\nh. Zamień wisdom na słowo friendship:\n", "", quote.replace('wisdom', 'friendship'))
