def sum_naturals_for(n):
    sum_nums = 0

    for number in range(1, n + 1):
        sum_nums += number
    return sum_nums


def sum_naturals_while(n):
    sum_nums = 0

    while n > 0:
        sum_nums = sum_nums + n
        n = n - 1
    return sum_nums


def sum_naturals_recursion(n):
    if n == 1:
        return 1
    return n + sum_naturals_recursion(n - 1)


print(sum_naturals_for(10))
print(sum_naturals_while(10))
print(sum_naturals_recursion(10))
