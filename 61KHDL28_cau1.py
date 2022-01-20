# Đề 28 câu 1
#a+b
L = []
with open('K61.txt') as f:
    for line in f:
        L.append(line)
newL = []
for i in L:
  newL.append(i.strip())
print('File K61.txt: ',newL)
#c in ra dòng có nhiều ký tự nhất
max = 0
for i in range(0, len(newL)):
    if len(newL[i]) > max:
        max = len(newL[i])

for i in range(0, len(newL)):
    if len(newL[i]) == max:
        print('Dong co nhieu ky tu nhat : ',newL[i])
#d tạo từ điển
D = {}
for i in range(len(newL)):
  D[i] = len(newL[i])
print('Tu dien D: ',D)
# e line có chứa 'a'
a_include = []
for i in range(len(newL)):
  if 'a' in newL[i]:
    a_include.append(i)
print("Thu tu dong co chua it nhat 'a': ",a_include)
