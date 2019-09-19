import matplotlib.pyplot as plt
import numpy as np
from decimal import getcontext, Decimal

getcontext().prec = int(input('getcontext().prec = '))

t = Decimal(input('t = '))
u = Decimal(input('u = '))
m = Decimal(input('m = '))
N = int(input('N = '))

s = 0
p = 1
q = 1
K = []
S = []
for k in range(N + 1):
    s += m ** (2 * k + 1) * (-1) ** (k % 2) * p * q
    K.append(k)
    S.append(s)
    p *= 1 - (t + 1) / (k + 1)
    q *= 1 - u / (k + 1)
    if k % 100000 == 0:
        print(k)

# plt.plot(np.array(K), np.array(S))
#
# plt.xlabel('y')
# plt.ylabel('f(y)')
# plt.grid(True)
# plt.show()

print(S[-3])
print(S[-2])
print(S[-1])
