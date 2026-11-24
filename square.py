import math


def _validate_dimensions(*values):
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Arguments must be int or float")
        if not math.isfinite(value) or value < 0:
            raise ValueError("Arguments must be finite non-negative numbers")


def area(a):
    """
    Вычисляет площадь квадрата.

    Аргументы:
        a (float): длина стороны квадрата.

    Возвращает:
        float: площадь квадрата.

    Пример вызова:
        >>> area(4)
        16
    """
    _validate_dimensions(a)
    return a ** 2


def perimeter(a):
    """
    Вычисляет периметр квадрата.

    Аргументы:
        a (float): длина стороны квадрата.

    Возвращает:
        float: периметр квадрата.

    Пример вызова:
        >>> perimeter(4)
        16
    """
    _validate_dimensions(a)
    return 4 * a
