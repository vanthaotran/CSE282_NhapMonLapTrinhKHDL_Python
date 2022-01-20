# Tạo một tập hợp gồm các số nguyên lẻ trong khoảng từ 1 đến 199, in chúng
# ra màn hình

L = [];
for i in range(1, 200):
    if i%2 == 1:
        L.append(i);

t = tuple(L);
print(t);