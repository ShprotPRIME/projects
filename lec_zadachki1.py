import numpy as np

a = [5, 6, 7]
b = np.array(a)

def math(b):
    x = sum(b) / len(b)
    return x

print(math(b))
