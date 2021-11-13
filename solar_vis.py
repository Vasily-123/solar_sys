# coding: utf-8
# license: GPLv3

import pygame as pg
import pygame.draw

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.5*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **r** координату по **r** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **r** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **r** — r-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Возвращает экранную **v** координату по **v** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **v** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **v** смотрела вверх.

    Параметры:

    **v** — v-координата модели.
    """
    return int(y*scale_factor) + window_height//2  # FIXME



if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen):
        self.screen = screen


    def update(self, figures, ui):
        self.screen.fill('white')
        for figure in figures:
            figure.draw(self.screen)
        
        ui.blit()
        ui.update()
        pg.display.update()


class DrawableObject:
    def __init__(self, obj):
        self.obj = obj
        #self.r = obj.r  # расстояние до солнца в начале
        self.R = obj.R  # радиус тела в пикселях
        self.color = obj.color
        self.x = obj.x
        self.y = obj.y
        self.type = obj.type
        self.m = obj.m
        self.Vx = obj.Vx
        self.Vy = obj.Vy
        self.v = (obj.Vx ** 2 + obj.Vy ** 2) ** (0.5)

    def draw(self, surface):
        pg.draw.circle(surface, self.color, (scale_x(self.x), scale_y(self.y)), self.R)
        pg.draw.circle(surface, 'black', (scale_x(self.x), scale_y(self.y)), self.R, 2)