from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def cicloid(R=10):
    t = np.arange(-2 * R, 2 * R, 0.1)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y
    

    plt.plot(x, y)
    plt.savefig('waves.png')
    plt.close()

def aster(R=8):
    t = np.arange(-2 * R/4, 2 * R, 0.1)
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    
    

    plt.plot(x, y)
    plt.savefig('asteroidi.png')
    plt.close()
    
if __name__ == '__main__':
    cicloid()
    aster()




