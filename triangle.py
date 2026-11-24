import math


def _validate_dimensions(*values):
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Arguments must be int or float")
        if not math.isfinite(value) or value < 0:
            raise ValueError("Arguments must be finite non-negative numbers")


def area(a, h):
    """
    Вычисляет площадь треугольника по стороне и высоте.

    Аргументы:
        a (float): длина основания треугольника.
        h (float): высота, проведённая к этому основанию.

    Возвращает:
        float: площадь треугольника.

    Пример вызова:
        >>> area(6, 4)
        12.0
    """
    _validate_dimensions(a, h)
    return a * h / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника по трём сторонам.

    Аргументы:
        a (float): первая сторона треугольника.
        b (float): вторая сторона треугольника.
        c (float): третья сторона треугольника.

    Возвращает:
        float: периметр треугольника.

    Пример вызова:
        >>> perimeter(3, 4, 5)
        12
    """
    _validate_dimensions(a, b, c)
    if not (a == 0 and b == 0 and c == 0):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality is violated")
    return a + b + c
