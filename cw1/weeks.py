# 1. Stwórz skrypt weeks.py. Napisz program, który obliczy i wyświetli liczbę minut w ciągu siedmiu tygodni.
print("Seven weeks equals", (((7 * 7) * 24) * 60), "minutes.")

# 2. Dokładnie 75 godziny. Tyle czasu wg. naukowców potrzeba, aby nabyć nową umiejętność. Oblicz ile pełnych tygodni
# zajmie Ci zdobycie nowej umiejętności, w zależności o tego, ile czasu jesteś wstanie poświęcić na naukę w tygodniu.
estimatedTime = float(75 / (4 + 4 + 1 + 1 + 1 + 3 + 3))
print("To acquire a new skill it will take me", round(estimatedTime, 1), "weeks.")
