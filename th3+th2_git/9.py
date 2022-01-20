# Nhập mảng a và b có 10 phần tử, tính khoảng cách
# euclid giữa a và b

import numpy as np
import math
a = np.random.randint(100, size = 10)
b = np.random.randint(100, size = 10)
print(a)
print(b)
d = 0
for i in range(10):
    d = d + (a[i]-b[i]**2)
d = math.sqrt(d)
print(d)