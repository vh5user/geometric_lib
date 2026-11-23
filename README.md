# geometric_lib

Небольшая Python-библиотека для вычисления площади и периметра простых геометрических фигур: круга, квадрата, прямоугольника и треугольника.

## Возможности

- площадь и длина окружности круга — `circle.py`
- площадь и периметр квадрата — `square.py`
- площадь и периметр прямоугольника — `rectangle.py`
- площадь и периметр треугольника — `triangle.py`

## Структура проекта

~~~text
geometric_lib
├── circle.py
├── square.py
├── rectangle.py
├── triangle.py
├── tests
│   ├── __init__.py
│   ├── test_circle.py
│   ├── test_square.py
│   ├── test_rectangle.py
│   └── test_triangle.py
├── docs
│   └── README.md
├── .gitignore
└── README.md
~~~

## Быстрый старт

Внешних зависимостей нет, нужен только Python версии 3 и выше.

~~~python
from circle import area, perimeter

print(area(3))       # 28.274333882308138
print(perimeter(3))  # 18.84955592153876
~~~

## Тестирование

В проекте реализовано 132 unit-теста на базе стандартного модуля `unittest` (по 33 теста на каждую фигуру).

Запуск всех тестов:

~~~bash
python -m unittest discover -s tests -v
~~~

Запуск тестов отдельного модуля (например, для прямоугольника):

~~~bash
python -m unittest tests/test_rectangle.py -v
~~~

## Документация

Полное описание каждой функции с примерами вызова, сведения о тестировании и история изменений — в [docs/README.md](docs/README.md). *Каждая функция также задокументирована прямо в коде* — в виде docstring, см. исходники файлов.
