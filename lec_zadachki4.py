import numpy as np

N = int(input("Размер N:"))
M = int(input("Размер M:"))

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        value = np.sin(N * i + M * j + 1)
        
        if value < 0:
            trigonometry_array[i, j] = 0
        else:
            trigonometry_array[i, j] = value
            
print(trigonometry_array)