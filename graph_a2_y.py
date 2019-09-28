import matplotlib.pyplot as plt
import numpy as np
from deflib.QED import b_table

y = int(input())
A = b_table({(i, y - i - 1) for i in range(y)})
t = np.arange(-y + 2, y + 1, 2)
s = np.array([A[i, y-i-1][1] for i in range(y)])
plt.plot(t, s)

plt.xlabel('x')
plt.ylabel('a_2(x, ' + str(y) + ')')
plt.grid(True)
plt.savefig("Graphics\\plot_a2_" + str(y) + ".png")
plt.show()
