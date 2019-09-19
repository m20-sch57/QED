import matplotlib.pyplot as plt
import numpy as np
from deflib.QED.xy_and_tu import t_u


def vec_a(x, y):
    t, u = t_u(x, y)

    if t < 0 or u < 0:
        return []

    A = [[(0, 0)] * (u + 1) for i in range(t + 1)]

    A[0][0] = (0, 1)

    for i in range(t + 1):
        for j in range(u + 1):
            if i != 0:
                A[i][j] = (A[i][j][0], A[i][j][1] - A[i - 1][j][0] + A[i - 1][j][1])
            if j != 0:
                A[i][j] = (A[i][j][0] + A[i][j - 1][0] + A[i][j - 1][1], A[i][j][1])

    return A


y = int(input())
A = vec_a(1, 2 * y - 1)
t = np.arange(y + 1)
s = np.array([sum([A[i][j-i-1][0] ** 2 for i in range(j)]) / 2 ** (j - 1) for j in range(y + 1)])
plt.plot(t, s)

plt.xlabel('y')
plt.ylabel('sum P(x, y, -)')
plt.grid(True)
plt.savefig("Graphics\\plot_sum_P_minus_" + str(y) + ".png")
plt.show()