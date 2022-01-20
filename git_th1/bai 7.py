a = int(input("Nhap a = "))
b = int(input("Nhap b = "))

for i in range(a, b+1):
    if(i%7==0) & (i%5!=0):
        print(i)