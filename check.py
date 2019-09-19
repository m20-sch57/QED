from QED3 import vec_a as vec_a3
from QED9 import vec_a as vec_a9

from QED import *

x, y = map(int, input().split())
t, u = t_u(x, y)

A3 = vec_a3(x, y)[0]
A9 = [[vec_a9(*x_y(i, j)) for j in range(u + 1)] for i in range(t + 1)]
print(A3)
print(A9)
print(A3 == A9)