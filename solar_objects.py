# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 1
    """Масса звезды"""

    x = 0
    """Координата по оси **r**"""

    y = 0
    """Координата по оси **v**"""

    Vx = 0
    """Скорость по оси **r**"""

    Vy = 0
    """Скорость по оси **v**"""

    Fx = 0
    """Сила по оси **r**"""

    Fy = 0
    """Сила по оси **v**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 1
    """Масса планеты"""

    x = 0
    """Координата по оси **r**"""

    y = 0
    """Координата по оси **v**"""

    Vx = 0
    """Скорость по оси **r**"""

    Vy = 0
    """Скорость по оси **v**"""

    Fx = 0
    """Сила по оси **r**"""

    Fy = 0
    """Сила по оси **v**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""