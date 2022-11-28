from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-3,4)
y1 = -x+6
y2 = x**2+1

plt.plot(x, y1, marker = 'o', linestyle = '--', color = 'b')
plt.plot(x, y2, marker = 'x', linestyle = '--', color = 'r')

plt.grid(True, axis='y', linestyle = '--', color ='r')
plt.show()

