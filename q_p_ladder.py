import matplotlib.pyplot as plt
import numpy as np
from deflib.QED import Q_set

d, L = map(int, input().split())


t = np.arange(-d, d + 1)
s = []
for i in range(-d, d+1):
    if i >= 0:
        s.append(Q_set(set((j, j+i) for j in range(L))))
    else:
        s.append(Q_set(set((j-i, j) for j in range(L))))

s = np.array(s)
plt.plot(t, s)

plt.xlabel('d')
plt.ylabel('Q(i + a, i)')
plt.grid(True)
plt.savefig("Graphics\\plot_Q(i+a,i).png")
plt.show()
