# Sinh ra một mảng số thực có
# 1000 phần tử, các phần tử nằm
# trong khoảng từ
# -0.5 đến <0.5

import numpy as np
a = np.random.random(size=100)
print(a)
# tịnh tiến b sang 0.5 đon vị [-0.5; 0.5]
b = a-0.5
print(b)