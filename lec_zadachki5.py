import math as m
Q = "Прямоугольничек"
a = 6
b = 7
def rectangle(a):
    x = a * b 
    return x

F = "Треугольничек"
a = 7
h = 2
def triangle(b):
    x = a * h / 2
    return x

R = "Кружочек"
r = 6
def circle(a):
    x = m.pi * r ** 2 
    return x 

ans = input(f"Выберите фигуру {Q}, {F}, {R}: ")
if ans == Q:
    print(rectangle(a))
elif ans == F:
    print(triangle(b))
elif ans == R:
    print(circle(a))
else:
    print("ОШИБА 0_0")
    

