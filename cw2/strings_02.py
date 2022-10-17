# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
s1 = "Fruit"
s2 = "Loops"
s1_center = len(s1) // 2
s3 = s1[:s1_center] + s2 + s1[s1_center:]

print("s1 = \"Fruit\"", "\ns2 = \"Loops\"", "\ns3 =", s3)
