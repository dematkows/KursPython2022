# 6. Przekopiuj zawartość import this do zmiennej.
print("\n6. Przekopiuj zawartość import this do zmiennej.")

variable = "The Zen of Python, by Tim Peters" \
           "\nBeautiful is better than ugly." \
           "\nExplicit is better than implicit." \
           "\nSimple is better than complex." \
           "\nComplex is better than complicated." \
           "\nFlat is better than nested." \
           "\nSparse is better than dense." \
           "\nReadability counts." \
           "\nSpecial cases aren't special enough to break the rules." \
           "\nAlthough practicality beats purity." \
           "\nErrors should never pass silently." \
           "\nUnless explicitly silenced." \
           "\nIn the face of ambiguity, refuse the temptation to guess." \
           "\nThere should be one-- and preferably only one --obvious way to do it." \
           "\nAlthough that way may not be obvious at first unless you're Dutch." \
           "\nNow is better than never." \
           "\nAlthough never is often better than *right* now." \
           "\nIf the implementation is hard to explain, it's a bad idea." \
           "\nIf the implementation is easy to explain, it may be a good idea." \
           "\nNamespaces are one honking great idea -- let's do more of those!"

# Policz liczbę wystąpień słowa better.
print("\na. Policz liczbę wystąpień słowa better.")
print("", variable.count("better"))

# Usuń z tekstu symbol gwiazdki
print("\nb. Usuń z tekstu symbol gwiazdki.")
print("After replacement:\n", variable.replace('*', ''))

# Zamień jedno wystąpienie explain na understand
print("\nc. Zamień jedno wystąpienie explain na understand.")
print("After replacement:\n", variable.replace('explain', 'understand', 1))

# Usuń spacje i połącz wszystkie słowa myślnikiem
print("\nd. Usuń spacje i połącz wszystkie słowa myślnikiem.")
print("After replacement:\n", variable.replace(' ', '-'))

# Podziel tekst na osobne zdania za pomocą kropki
print("\ne. Podziel tekst na osobne zdania za pomocą kropki.")
print("After splitting:")
print(variable.split('.'))
