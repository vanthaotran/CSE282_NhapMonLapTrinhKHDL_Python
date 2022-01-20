import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,4,5,6,7])
y = np.array([2,6,3,6,3])

plt.plot(x,y,'o:r')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')
plt.show()