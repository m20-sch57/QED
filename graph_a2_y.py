import matplotlib.pyplot as plt
import numpy as np
from QED.QED3 import vec_a

y = int(input())
A = vec_a(1, 2 * y - 1)[0]
t = np.arange(-y + 2, y + 1, 2)
s = np.array([A[i][y-i-1][1] / 2 ** ((y - 1) / 2) for i in range(y)])
plt.plot(t, s)

plt.xlabel('x')
plt.ylabel('a_2(x, ' + str(y) + ')')
plt.grid(True)
plt.savefig("Graphics\\plot_a2_" + str(y) + ".png")
plt.show()