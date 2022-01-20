# Cho một dãy số tự nhiên 20 phần tử,
# hãy thay thế tất cả những phần tử lẻ bằng
# số -1

import numpy as np
a = np.random.randint(100, size = 20)
for i in range(len(a)):
    if a[i] % 2 == 1:
        a[i] = -1

print(a)