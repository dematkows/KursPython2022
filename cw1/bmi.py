# 1. Stwórz plik bmi.py i napisz program, który obliczy BMI.
# Wzór jest bardzo prosty:#
# BMI = (masa (kg)) / (wzrost (m))²
weight = float(input("Enter your weight [kg]: "))
height = float(input("Enter your height [m]: "))
bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))
