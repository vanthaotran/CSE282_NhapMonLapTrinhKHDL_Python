# Đề 24 câu 1
#a
s = input().split(',') # nhập dãy số nhị phân
L = []
for i in s:
  L.append(i)
print("L:",L)
#b chuyển nhị phân sang thập phân
L1 = []
for i in L:
    c = 0
    for j in i:
        c = c*2+int(j)
    L1.append(c)
print("L1:",L1)
# c sắp xếp L1
print(sorted(L1,reverse=False))
# d số nguyên tố trong L1
for i in L1:
    count=0
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
    if(count==0):
        print('So nguyen to ',i)
#e phương sai các số trong L1
import statistics
print('Phuong sai cac so trong L1: ',statistics.variance(L1))
