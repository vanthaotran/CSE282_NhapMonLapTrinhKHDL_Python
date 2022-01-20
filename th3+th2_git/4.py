# Hai mảng a và b có cùng số dòng,
# hãy ghép chúng theo các dòng thành mảng
# c, các cột của a rồi đến các cột của b

import numpy as np
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9], [1,2,3]])

c = np.concatenate([a,b], axis=1)
print(c)
d = np.concatenate([a,b], axis=0)
print(d)

# random ngẫu nhiên mảng
# a = np.random.randint(100, size = [4,5])
# print(a)