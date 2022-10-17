# 5. W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""

# Zadbaj o sposób wyświetlania np.:
# szybko : 5
# zbudź : 1

txt = """Szybko, zbudź się, szybko, wstawaj
    Szybko, szybko, stygnie kawa
    Szybko, zęby myj i ręce"""

print(txt)
print()
txt = txt.lower()
txt = txt.replace(",", "")
txt = txt.split()

# 1.
uniq_word = set(txt)

for word in uniq_word:
    print(f"{word}: {txt.count(word)}")
print()

# 2.
counting_dict = {}

for w in txt:
    if w not in counting_dict:
        counting_dict[w] = 1
    else:
        counting_dict[w] += 1

for k, v in counting_dict.items():
    print(k, ":", v)
print()
