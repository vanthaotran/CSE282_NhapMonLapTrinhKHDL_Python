a = int(input("Nhap so a = "));
b = int(input("Nhap so b = "));

for i in range(a,b+1):
    count = 0
    for j in range (2, i//2+1):
        if (i % j==0):
            count += 1
    if (count == 0):
        print("So nguyen to ",i)