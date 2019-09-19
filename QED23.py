import matplotlib.pyplot as plt
import numpy as np


def f(L):
    def m(x, y):
        if x == 1:
            return -0.2
        if x == L:
            return 0.2
        return 0

    def init_a(x):
        x -= 1
        if x % 2:
            return 0
        x //= 2
        if x % 2:
            x = (x - 1) // 2
            return 1 / 2 ** 0.5 if (x + 1) % 4 < 2 else -1 / 2 ** 0.5, 1 / 2 ** 0.5 if x % 4 < 2 else -1 / 2 ** 0.5
        else:
            x //= 2
            return (0, (-1) ** (x % 4 // 2)) if not x % 2 else ((-1) ** ((x - 1) % 4 // 2), 0)

    def rotate(vec):
        return (vec[1], -vec[0])

    y = 2 * L

    if y % 2:
        return 0

    # A_yx
    A = [[{'+': (0, 0), '-': (0, 0)}] * (2 * (y - i) + 1) for i in range(y + 1)]

    for i in range(1, y + 1):
        for j in range(-(y - i), (y - i) + 1, 2):
            if i == 1:
                A[i][j + y - i] = {'+': init_a(j), '-': (0, 0)}
            else:
                x_1 = A[i-1][j-1 + y - i + 1]['+']
                x_2 = rotate(A[i-1][j-1 + y - i + 1]['-'])
                y_1 = A[i-1][j+1 + y - i + 1]['-']
                y_2 = rotate(A[i-1][j+1 + y - i + 1]['+'])
                A[i][j + y - i] = {'+': ((x_1[0] + x_2[0] * m(j-1, i-1))/(1 + m(j-1, i-1) ** 2) ** 0.5,
                                         (x_1[1] + x_2[1] * m(j-1, i-1))/(1 + m(j-1, i-1) ** 2) ** 0.5),
                                   '-': ((y_1[0] + y_2[0] * m(j+1, i-1))/(1 + m(j+1, i-1) ** 2) ** 0.5,
                                         (y_1[1] + y_2[1] * m(j+1, i-1))/(1 + m(j+1, i-1) ** 2) ** 0.5)}

    return A[y][0]

# TODO: ПЕРЕПИСАТЬ!

N = int(input())
A = np.arange(3, 2 * N + 1, 2)
B = np.array(list(map(lambda d: d['-'][0] ** 2 + d['-'][1] ** 2, [f(L) for L in A])))
plt.plot(A, B)

plt.xlabel('L')
plt.ylabel('f(L)')
plt.grid(True)
plt.savefig("Graphics\\plot_f(L)_" + str(N) + ".png")
plt.show()