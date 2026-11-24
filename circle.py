import math


def _validate_dimensions(*values):
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Arguments must be int or float")
        if not math.isfinite(value) or value < 0:
            raise ValueError("Arguments must be finite non-negative numbers")


def area(r):
    """
    Вычисляет площадь круга.

    Аргументы:
        r (float): радиус круга.

    Возвращает:
        float: площадь круга.

    Пример вызова:
        >>> area(3)
        28.274333882308138
    """
    _validate_dimensions(r)
    return math.pi * r ** 2


def perimeter(r):
    """
    Вычисляет длину окружности (периметр круга).

    Аргументы:
        r (float): радиус круга.

    Возвращает:
        float: длина окружности.

    Пример вызова:
        >>> perimeter(3)
        18.84955592153876
    """
    _validate_dimensions(r)
    return 2 * math.pi * r
