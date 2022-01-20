# Sinh một ma trận 3x5 gồm các số ngẫu nhiên từ 0 đến nhỏ hơn 10, tính và in
# ra số lớn nhất trên mỗi dòng của ma trận

import numpy as np
a = np.random.randint(10, size=(3,5))
print(a)
# x = a[0][0]
# print(x)
for line in range(0,3):
    for i in range(0,5):
        max_line = a[i][j]
        # if a[i][j] > max_line:

# idea:
# - khai báo thư viện
# - tạo mảng random
# - duyệt từng dòng của mảng, chọn phần từ đầu tiên của dòng i đó so sánh
# nếu phần tử thứ j của dòng i lớn hơn phần tử đầu tiên đó thì đó chính là giá trị in ra

