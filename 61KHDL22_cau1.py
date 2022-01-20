# Đề 22 câu 1
#a
ss = input()
s = ss.split()
print(s)
#b in ra từ có độ dài dài nhất
sorted_words = sorted(s,key=len)
print("Tu dai nhat: ", (sorted_words[-1]))
#c tao tu dien
D = {}
a = len(s)
while a>0:
  key = s[0]
  dem=0
  j=0
  while j<len(s):
    if s[j]==key:
      dem=dem+1
      s=s[0:j]+s[j+1:]
    else:
      j=j+1
  D[key]=dem
  a=len(s)
print(D)
#d sắp xếp từ điển
sorted_values = sorted(D.values())
sorted_dict = {}
for i in sorted_values:
  for k in D.keys():
    if D[k] == i:
      sorted_dict[k] = D[k]
print('Tu dien sap xep: ',sorted_dict)
# e
sum_ = 0
numbers = []
for num in ss:
    if num.isdigit():
        sum_ += int(num)**2
        numbers.append(num)
print("\nTổng bình phương các số trong chuỗi là:", sum_)
print("\nChuỗi có", len(numbers), "ký tự số đó là:", *numbers)
