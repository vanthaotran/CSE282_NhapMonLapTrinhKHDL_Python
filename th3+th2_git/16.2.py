# Đọc 1 file, tìm và in ra nội dung của
# dòng dài nhất trong file đó

L = []
with open('1951061116.txt') as f:
    for line in f:
        L.append(line)

max = 0
for i in range(0, len(L)):
    if len(L[i]) > max:
        max = len(L[i])

for i in range(0, len(L)):
    if len(L[i]) == max:
        print(L[i])