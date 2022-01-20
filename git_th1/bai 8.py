# cau a
n = int(input("Nhap n = "));
result = 0
import math

# print(math.factorial(5))
for i in range(1, n+1):
    result += 1/(math.factorial(i))

print(result)

# cau b
# n = int(input("Nhap n = "));
# import math
# result = 0
#
# for i in range(2, n+1):
#     mau = (i-1)*i
#     result += 1+(1/mau)
#
# print(result)

#cau c
n = int(input("Nhap n = "));
import math
result = 0

for i in range(2, n+1):
    result += pow(-1,i-1)/math.factorial(i)

print(result)
