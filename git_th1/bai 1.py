import math
a = int(input("Nhap so a = "));

ktra = True
if(a<2):
    ktra = False
for i in range (2, a):
    if(a%i==0):
        ktra = False

print(ktra)
