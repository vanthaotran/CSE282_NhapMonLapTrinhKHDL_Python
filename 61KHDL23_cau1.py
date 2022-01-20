# Đề 23 câu 1
ss = input()
s = ss.split()
print(s)

L = []
#a+b
for i in s:
  L.append(i)
print('L:',L)
#c
L.sort()
print('Sap xep L: ',L)
#d
longest = max(L,key=len)
print('Tu dai nhat: ',longest)
#e
sum_of_squares = 0
nums = []
for num in ss:
    if num.isdigit():
        sum_of_squares += int(num)**2
        nums.append(num)
print("\nTổng bình phương các số trong chuỗi là:", sum_of_squares)
print("\nChuỗi có", len(nums), "ký tự số đó là:", *nums)
