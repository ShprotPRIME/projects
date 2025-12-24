from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

frames = 100

x0 = 0.1
y0 = 0.1 
C = 0.3
D = 0.33

x = [x0]
y = [y0]

for n in range(frames):
    x.append(x[n-1]**2 - y[n-1]**2 + C)
    y.append(2 * x[n-1] * y[n-1] + D)
    
    
fig, ax = plt.subplots() 
    
anim_object, = plt.plot([], [], '-', lw=2)

ax.set_xlim(-0.5, 0,5)
ax.set_ylim(-0.5, 0.5)

def update(frame):
    x.append(frame)
    y.append(np.sin(frame)) 
    anim_object.set_data(x, y)
    return anim_object

ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames, # Интервал значений
                    interval=50) # Интервал между кадрами,
                                 # по умолчанию 200 милисекунд

ani.save('animation_1.gif', writer="pillow")
