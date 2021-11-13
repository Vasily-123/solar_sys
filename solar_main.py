# coding: utf-8
# license: GPLv3

from solar_vis import *
from solar_model import *
from solar_input import *
import thorpy
import time
import numpy as np

timer = None

alive = True

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

model_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

time_scale = 100.0
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""

in_filename = ''

def execution(delta):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global model_time
    global displayed_time
    recalculate_space_objects_positions([dr for dr in space_objects], delta)
    model_time += delta

def write_to_written():
    write_space_objects_data_to_file("written.txt", space_objects)

def write_to_stats():
    global model_time
    output = open("stats.txt", 'w')
    output.close()

def append_to_stats():
    global in_filename
    global model_time
    if in_filename == "one_satellite.txt":
        for obj in space_objects:
            if obj.type == 'planet':
                output = open("stats.txt", 'a')
                r = (obj.x ** 2 + obj.y ** 2) ** (0.5)
                v = obj.v
                t = model_time
                print(' '.join(["{:.0f}".format(item) for item in [r, v, t]]), file=output)
                output.close()


def start_execution():
    """Обработчик события нажатия на кнопку Play.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True


def pause_execution():
    global perform_execution
    perform_execution = False


def stop_execution():
    """Обработчик события нажатия на кнопку Pause.
    Останавливает циклическое исполнение функции execution.
    """
    global alive
    alive = False


def open_file_0():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global browser
    global model_time
    global in_filename

    model_time = 0.0
    in_filename = "solar_system.txt"
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

def open_file_1():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global browser
    global model_time
    global in_filename

    model_time = 0.0
    in_filename = "written.txt"
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)


def open_file_2():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global browser
    global model_time
    global in_filename

    model_time = 0.0
    in_filename = "double_star.txt"
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

def open_file_3():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global browser
    global model_time
    global in_filename

    model_time = 0.0
    in_filename = "one_satellite.txt"
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

def handle_events(events, menu):
    global alive
    for event in events:
        menu.react(event)
        if event.type == pg.QUIT:
            alive = False


def slider_to_real(val):
    return np.exp(5 + val)


def slider_reaction(event):
    global time_scale
    time_scale = slider_to_real(event.el.get_value())


def init_ui(screen):
    global browser
    slider = thorpy.SliderX(100, (-12, 12), "Simulation speed")
    slider.user_func = slider_reaction
    button_stop = thorpy.make_button("Quit", func=stop_execution)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
    timer = thorpy.OneLineText("Seconds passed")

    button_write = thorpy.make_button("Safe data", func=write_to_written)
    button_load1 = thorpy.make_button(text="Load start", func=open_file_0)  # params = {0}, 1, 2 ...
    button_load2 = thorpy.make_button(text="Load last", func=open_file_1)
    button_load3 = thorpy.make_button(text="Double star", func=open_file_2)
    button_load4 = thorpy.make_button(text="Satelitte", func=open_file_3)


    box = thorpy.Box(elements=[
        slider,
        button_pause,
        button_stop,
        button_play,
        button_load1,
        button_load2,
        button_load3,
        button_load4,
        button_write,
        timer])
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    box.add_reaction(reaction1)

    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((100, 100))
    box.blit()
    box.update()
    return menu, box, timer


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """

    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global perform_execution
    global timer

    print('Modelling started!')
    physical_time = 0

    pg.init()

    width = 1000
    height = 900
    screen = pg.display.set_mode((width, height))
    last_time = time.perf_counter()
    drawer = Drawer(screen)
    menu, box, timer = init_ui(screen)
    write_to_stats()

    while alive:
        handle_events(pg.event.get(), menu)
        cur_time = time.perf_counter()
        if perform_execution:
            execution((cur_time - last_time) * time_scale)
            text = "%d seconds passed" % (int(model_time))
            timer.set_text(text)
            append_to_stats()

        last_time = cur_time
        drawer.update(space_objects, box)
        time.sleep(1.0 / 60)
    print('Modelling finished!')


if __name__ == "__main__":
    main()
