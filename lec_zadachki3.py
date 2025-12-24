from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def serdechko(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return [x], [y]


fig, ax = plt.subplots()
serdce, = plt.plot([], [], 'o', color='r', label='Ball')

frames = np.arange(0, 2*np.pi, 0.1)

def animate(t):
    serdce.set_data(serdechko(t=t))
    return serdechko


plt.axis('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('serdechko.gif', writer="pillow")