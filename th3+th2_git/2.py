# Cho một dãy số nguyên 100 phần tử,
# hãy tách lấy tất cả những phần tử lẻ cho
# vào một mảng

import numpy as np
a = np.random.randint(100, size = 100)
b = a[a%2==1]
print(b)