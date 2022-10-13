# Czy string zawiera conajmniej 1 duzą literę
txt = 'ABRACADABRA'
txt.isupper()
txt = 'abracaDAbra'

# 1. Tekst składa się tylko z liter & tekst nie zawiera tylko małych
print("Is a string alphabetic & at least one uppercase?:", txt.isalpha() and not txt.islower())
