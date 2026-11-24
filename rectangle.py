import math


def _validate_dimensions(*values):
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Arguments must be int or float")
        if not math.isfinite(value) or value < 0:
            raise ValueError("Arguments must be finite non-negative numbers")


def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Аргументы:
        a (float): первая сторона прямоугольника.
        b (float): вторая сторона прямоугольника.

    Возвращает:
        float: площадь прямоугольника.

    Пример вызова:
        >>> area(4, 5)
        20
    """
    _validate_dimensions(a, b)
    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Аргументы:
        a (float): первая сторона прямоугольника.
        b (float): вторая сторона прямоугольника.

    Возвращает:
        float: периметр прямоугольника.

    Пример вызова:
        >>> perimeter(4, 5)
        18
    """
    _validate_dimensions(a, b)
    return 2 * (a + b)
