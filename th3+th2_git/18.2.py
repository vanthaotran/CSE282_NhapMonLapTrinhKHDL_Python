#  Đọc 1 file, thống kê và in ra tất
#  cả các chữ cái có trong file và số lần xuất
# hiện của các chữ đó

L = [] # key
D = {}
with open('1951061116.txt') as f:
    for line in f:
        line.replace('\n', ' ')
        L1 = line.split()
        L = L + L1
    for i in L:
        if i in D:
            D[i] += i
        else:
            D[i] = 1
print(sorted(D.items(), key = lambda x:x[1]))
