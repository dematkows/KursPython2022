# 2. Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

l_test = [1, 2, 3, 4]
t_test = (1, 2, 3, 4)
s_test = {1, 2, 3, 4}

print("For tuple won't work:"
      "\n.append()"
      "\n.sort()"
      "\n.remove()"
      "\n.clear()"
      "\n.copy()"
      "\n.extend()"
      "\n.insert()"
      "\n.pop()"
      "\n.reverse()")

print("\nFor set won't work:"
      "\n.append()"
      "\n.sort()"
      "\n.extend()"
      "\n.insert()"
      "\n.reverse()")
