from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def cicloid(R=10):
    t = np.arange(-2 * R, 2 * R, 0.1)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y
    
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Trajectory')


def animate(R):
    ball.set_data(cicloid(R=R))
    return ball


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('cicloid_anim.gif', writer="pillow")