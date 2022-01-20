# Tạo một tập hợp gồm các phần tử từ 0 đến 99, in chúng ra màn hình

L = [];
for i in range(0, 100):
    L.append(i);
t = tuple(L);
print(t);