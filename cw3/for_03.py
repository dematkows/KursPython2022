# 3. Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6,
# 10, 15, 21, 28, 36, 45, 55

sum_nums = 0
for number in range(1, 11):
    sum_nums += number
    print(sum_nums)
