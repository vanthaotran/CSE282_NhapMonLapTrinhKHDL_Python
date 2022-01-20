import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3])
y = np.array(([2, 4, 0]))

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph')

plt.plot(x, y)
plt.show()