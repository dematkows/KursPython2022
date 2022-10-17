# 1. Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub
# białym znakiem). Następnie powitaj każdą osobę na liście.
names = str(input("Give some names separated by whitespace: "))
names_list = names.split(' ')

for name in names_list:
    print("Hey", name + "!")
