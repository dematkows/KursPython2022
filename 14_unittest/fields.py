def check_values(*values):
    for item in values:
        if not isinstance(item, (int, float)):
            raise TypeError("Side has to be a numeric value!")


def square_area(side):
    check_values(side)
    return side * side


def rectangle_area(a, b):
    check_values(a, b)
    return a * b


def triangle_area(a, b):
    check_values(a, b)
    return a * b * 0.5


def trapezoid_area(a, b, h):
    check_values(a, b, h)
    return ((a + b) * h) / 2
