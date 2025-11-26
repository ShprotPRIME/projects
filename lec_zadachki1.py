import numpy as np 
import random

array1 = [random.randint(0, 100) for i in range(10)]    
array2 = [random.randint(0, 100) for i in range(10)]  
array3 = [random.randint(0, 100) for i in range(10)]  

array1 = np.array(array1)
array2 = np.array(array2)
array3 = np.array(array3)

print(max(max(array1), max(array2), max(array3)))
print(sum(array1) + sum(array2) + sum(array3))
    