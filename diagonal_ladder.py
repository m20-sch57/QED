import matplotlib.pyplot as plt
import numpy as np
from deflib.QED import Q_set

d, L = map(int, input().split())
d_len = len(str(d))

t = np.arange(0, d + 1)
s = np.array([Q_set(set((i + j, i + j) for j in range(L))) for i in range(d + 1)])
plt.plot(t, s)

plt.xlabel('d')
plt.ylabel('Q(i + a, i + a)')
plt.grid(True)
plt.savefig("Graphics\\plot_Q(i+a,i+a).png")
plt.show()
