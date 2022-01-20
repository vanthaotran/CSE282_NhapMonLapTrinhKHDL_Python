# Đọc 1 file, tìm và in ra từ dài nhất trong file

L = []
with open('1951061116.txt') as f:
    for line in f:
        line.replace('\n', ' ')
        L1 = line.split()
        L = L+L1
max = L[0]
for i in range(0, len(L)):
    if len(L[i]) > len(max):
        print(L[i])
        break
