import matplotlib.pyplot as plt
import numpy as np
from deflib.QED import Q_table


y = int(input())
A = Q_table({(i, y - i - 1) for i in range(y)}, sign='-')
t = np.arange(1, y + 1)
s = np.array([sum([A[i, j - i] for i in range(j + 1)]) for j in range(y)])
plt.plot(t, s)

plt.xlabel('y')
plt.ylabel('sum P(_, y, -)')
plt.grid(True)
plt.savefig("Graphics\\plot_sum_P(y,-)_" + str(y) + ".png")
plt.show()
