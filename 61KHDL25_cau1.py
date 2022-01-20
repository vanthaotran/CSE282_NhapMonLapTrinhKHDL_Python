# Đề 25 câu 1
D = {}
#a
print("Nhap tu dien cua ban. ")
yesNo = 'c'
L = []
while yesNo == 'c':
  key = input("Nhap key: ")
  value = input("Nhap value: ")
  D[key] = value
  L.append(value)
  yesNo = input('c/k: ')
print("Tu dien cua ban: D = ",D)
#b tổng value in L
for i in range(0, len(L)):
  L[i] = int(L[i])
print("Sum of L's values: ", sum(L))
#c sắp xếp và in ra từ điển
L.sort(reverse=False)
print('Sap xep value cua tu dien: ',L)
#d in ra số nguyên tố có trong values đó
for i in L:
    count=0
    if i < 2:
      continue
    for j in range(2,i//2+1):
        if(i%j==0):
            count+=1
    if(count==0):
        print('So nguyen to ',i)
#e
binary_list = []
for i in L:
  temp = "{0:b}".format(i)
  binary_list.append(temp)
print('Nhi phan: ', binary_list)
