# Đề 27 câu 1
n = int(input('n = '))
L = []
L1 = []
# a L1 là bình phương
for i in range(0,n):
  L1.append(i*i)
print("L1 (binh phuong cac so 0-n)=",L1)
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Hay nhap n > 0")
elif n == 1:
   print("Day fibo chay den: ",n,":")
   print(n1)
else:
   while count < n:
       L.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("L(Fibo sequence)=",L)
# b euclid distance L vs L1
import numpy as np
a = np.array(L)
b = np.array(L1)
dist = np.linalg.norm(a-b)
print('Euclid distance: ',dist)
# c tu dien D
zip_iterator = zip(L,L1)
D = {}
D = dict(zip_iterator)
print('Tu dien D: ',D)
# d số nguyên tố trong L
for i in L:
    count=0
    if i == 0:
      continue
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
    if(count==0):
        print('So nguyen to ',i)
#d convert int - binary
binary_list = []
for i in L:
  binary_list.append(format(10,'b'))
print('So nhi phan L: ', binary_list)
