from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection="3d")


t = np.arange(0.01, 4 * np.pi, 0.01)
R = 1


x = R * np.cos(t)
y = R * t ** 0.5
z = R * np.log10(t)


ax.plot(x, y, z, label='Dich')


arrow_x0 = 0
arrow_y0 = 0
arrow_z0 = 0


arrow_x1 = 1
arrow_y1 = 1
arrow_z1 = 1


ax.quiver(arrow_x0, arrow_x0, arrow_x0,
          arrow_x1, arrow_x1, arrow_x1,
          length=1, normalize=True, color='r')


ax.legend()


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


ax.set_title('3D Test')

plt.show()