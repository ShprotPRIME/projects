import numpy as np 
import random

N = int(input("Введите длинну массива:"))

for i in range(3):
    array = [random.randint(0, 100) for i in range(N)]    

array = np.array(array)
print(array)

a = list(zip(array))
print(max(array))