n = int(input("Nhap so n = "))
sum = 0
for i in range(1, n):
    if (n%i == 0):
        sum+= i

if (sum == n):
    print("La so hoan hao")
else:
    print("Khong la so hoan hao")