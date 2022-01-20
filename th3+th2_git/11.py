import matplotlib.pyplot as plt
import numpy as np

x_green = np.array([10, 20, 30])
y_green = np.array([40, 10, 30])

x_blue = np.array([10, 20, 30])
y_blue = np.array([20, 40, 10])

plt.plot(x_green, y_green)
plt.plot(x_blue, y_blue)
plt.title('Tưo ỏ moẻ lines on same plot ưith suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.show()