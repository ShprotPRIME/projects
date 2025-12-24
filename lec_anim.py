from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Задание траектории
N = 100
alpha = np.linspace(0, 10, N)

x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

# Создание анимируемых объектов
ball, = ax.plot(x, y, z, 'o', color='b')
line, = ax.plot(x, y, z, '-', color='b')


# Функция подстановки координат в анимируемые объекты
def animate(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])

    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])


# Украшательсвта и масштабирование
# ax.set(xlim3d=(0, 1), xlabel='X')
# ax.set(ylim3d=(0, 1), ylabel='Y')
# ax.set(zlim3d=(0, 1), zlabel='Z')

ani = FuncAnimation(fig, animate, N, interval=30)

# plt.show()
ani.save('simple.gif')