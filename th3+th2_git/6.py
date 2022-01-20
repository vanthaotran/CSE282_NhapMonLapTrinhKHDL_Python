# : Cho một mảng a, hãy in ra tất cả những phần tử trong khoảng từ 5 đến 1

import numpy as np
a = np.random.randint(100, size=(2,3))
print(a)
for i in range(0, 2):
    for j in range(0,3):
        # print(a[i][j])
        if a[i][j] < 5 and a[i][j] > 1:
            print(a[i][j])
        else:
            break