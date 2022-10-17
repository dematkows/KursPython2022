# 2. Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym. Zamianę z systemu
# binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).
# Prostszy sposób
decimal = (1 * 2 ** 6) \
          + (0 * 2 ** 5) \
          + (0 * 2 ** 4) \
          + (1 * 2 ** 3) \
          + (1 * 2 ** 2) \
          + (1 * 2 ** 1) \
          + (1 * 2 ** 0)

print("\n(Easy way) Binary number 1001111 is", decimal, "in decimal.")

# Trudniejszy sposób
bin_num = "1001111"
i = len(bin_num) - 1
first = int(bin_num[0])
second = int(bin_num[1])
third = int(bin_num[2])
fourth = int(bin_num[3])
fifth = int(bin_num[4])
sixth = int(bin_num[5])
seventh = int(bin_num[6])

decimal = (first * 2 ** i) \
          + (second * 2 ** (i - 1)) \
          + (third * 2 ** (i - 2)) \
          + (fourth * 2 ** (i - 3)) \
          + (fifth * 2 ** (i - 4)) \
          + (sixth * 2 ** (i - 5)) \
          + (seventh * 2 ** (i - 6))

print("(Hard way) Binary number", bin_num, "is", decimal, "in decimal.")
