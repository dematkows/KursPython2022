# 7. Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku:
# niedowaga / waga normalna / nadwaga / otyłość.

weight = float(input("Enter your weight [kg]: "))
height = float(input("Enter your height [m]: "))
bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18:
    print("Underweight!")
elif bmi <= 25:
    print("Optimal weight")
elif bmi <= 30:
    print("Overweight!")
else:
    print("You're obese!")
