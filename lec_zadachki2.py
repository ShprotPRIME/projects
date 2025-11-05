import lec_const_module as con
import math 

h = 100
a = 45
B = 35
v = math.sqrt(con.g * h * math.tan(B) ** 2 / 2 * math.cos(a) ** 2 * (1 - math.tan(B) * math.tan(a)))
print(v)
 
T = 200
f = 300 
N = 2 / math.sqrt(math.pi) * math.sqrt(con.h) * (con.k * T) ** 3/2 * con.e ** f/con.k/T * f ** T/2
print(N)