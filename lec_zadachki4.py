import matplotlib.pyplot as plt
import numpy as np

k = 0.3 

phi = np.arange(0, 8*np.pi, 0.001)
r = k / phi**0.5

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.savefig('spiralka.png')