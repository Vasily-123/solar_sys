import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

fig = plt.figure(figsize=(8, 8))
vt = fig.add_subplot(2, 2, 1)  # будет рисовать два на два графика, этот под номером 1
rt = fig.add_subplot(2, 2, 2)  # будет рисовать два на два графика, этот под номером 1
vr = fig.add_subplot(2, 2, 3)
r = []
v = []
t = []

f = open('stats.txt', 'r')
for line in f:
     if len(line.strip()) == 0:
          continue
     r.append(int(line.split(' ')[0]))  # по умолчанию разделение в каждой строке идёт по ' '
     v.append(int(line.split(' ')[1]))
     t.append(int(line.split(' ')[2]))

'''major_ticks = np.arange(min(r), max(r), 50)
major1_ticks = np.arange(min(v), max(v), 0.1)
minor1_ticks = np.arange(10, 500, 10)
minor_ticks = np.arange(10, 500, 10)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major1_ticks)
ax.set_yticks(minor1_ticks, minor=True)'''

def draw_ticks(name):
     name.xaxis.set_minor_locator(AutoMinorLocator())

     name.tick_params(which='both', width=2)
     name.tick_params(which='major', length=7)
     name.tick_params(which='minor', length=4, color='r')

     name.grid(which='minor', alpha=0.2)
     name.grid(which='major', alpha=0.5)

draw_ticks(vt)
draw_ticks(rt)
draw_ticks(vr)

x1 =np.linspace(0, 5, 20)  # Массив, в котором авномерно распределены 20 точек внутри отрезка 0,5

plt.grid(True)
vt.plot(t, v, 'o')
rt.plot(t, r, 's')
vr.plot(r, v, '^', label ='Смоделированная зависимость V(R)')


plt.xlabel(r'$R, м$')
plt.ylabel(r'$V, м/с$')
plt.legend(loc='best', fontsize=10)
'''
vt.label(r'$R, км$')
vt.label(r'$V, км/с$')
vt.legend(loc='best', fontsize=10)
rt.xlabel(r'$t, c$')
rt.ylabel(r'$R, км$')
rt.legend(loc='best', fontsize=10)'''


plt.title('Графики для спутника Солнца')
plt.show()



