# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <r> <v> <Vx> <Vy>

    Здесь (r, v) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """
    star.type = line.split()[0].lower()
    star.R = float(line.split()[1].lower())
    star.color = line.split()[2].lower()
    star.m = float(line.split()[3].lower())
    star.x = float(line.split()[4].lower())
    star.y = float(line.split()[5].lower())
    star.Vx = float(line.split()[6].lower())
    star.Vy = float(line.split()[7].lower())


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:

    Planet <радиус в пикселах> <цвет> <масса> <r> <v> <Vx> <Vy>

    Здесь (r, v) — координаты планеты, (Vx, Vy) — скорость.

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.

    **planet** — объект планеты.
    """
    planet.type = line.split()[0].lower()
    planet.R = float(line.split()[1].lower())
    planet.color = line.split()[2].lower()
    planet.m = float(line.split()[3].lower())
    planet.x = float(line.split()[4].lower())
    planet.y = float(line.split()[5].lower())
    planet.Vx = float(line.split()[6].lower())
    planet.Vy = float(line.split()[7].lower())


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <r> <v> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <r> <v> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    output = open(output_filename, 'w')
    print('#Данные о космических объектах', file=output)
    for obj in space_objects:
        print(''.join(str(obj.type)), ''.join(str(obj.R)),''.join(str(obj.color)),''.join(str(obj.m)),
              ''.join(str(obj.x)), ''.join(str(obj.y)), ''.join(str(obj.Vx)), ''.join(str(obj.Vy)), file=output)
    output.close()


if __name__ == "__main__":
    objects = read_space_objects_data_from_file('solar_system.txt')


