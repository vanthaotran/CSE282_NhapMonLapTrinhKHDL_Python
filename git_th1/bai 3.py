# UCLN va BCNN
a = int(input("Nhap a = "));
b = int(input("Nhap b = "));

a1 = a
b1 = b
while(a != b):
    if (a>b) :
        a = a - b
    else:
        b = b - a
print("UCLN: ",a)
print("BCNN: ",a1*b1/a)
