# Mảng a và b có cùng số cột,
# hãy ghép chúng theo các cột thành mảng c, các
# dòng của a rồi đến của b

import numpy as np
a = np.random.randint(100, size = [4,3])
b = np.random.randint(50, size = [1,5])

c = np.concatenate([a,b], axis=0)
print(c)
d = np.concatenate([a,b], axis=1)
print(d)