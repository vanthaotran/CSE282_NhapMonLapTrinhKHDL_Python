# bai 4
import math

# Nhap 3 canh
a = input("Nhap toa do diem A: ").split()
xA = int(a[0])
yA = int(a[1])

b = input("Nhap toa do diem B: ").split()
xB = int(b[0])
yB = int(b[1])

c = input("Nhap toa do diem C: ").split()
xC = int(c[0])
yC = int(c[1])

# Tinh khoang cach giua cac canh
# AB
ab = math.sqrt(math.pow(xB - xA, 2) + math.pow(yB - yA, 2))
ac = math.sqrt(math.pow(xC - xA, 2) + math.pow(yC - yA, 2))
bc = math.sqrt(math.pow(xC - xB, 2) + math.pow(yC - yB, 2))


if (ab+ac>bc) & (ab+bc>ac) & (ac+bc>ab) :
    print("ABC la tam giac")
    if (ab == ac) | (ab == bc) | (ac == bc):
        print("ABC la tam giac can")
        if(ab == ac) & (ab == bc):
            print("ABC la tam giac deu")
        if (math.pow(ab,2) == math.pow(ac,2)+math.pow(bc,2)) | (math.pow(bc,2) == math.pow(ab,2)+math.pow(ac,2)) | (math.pow(ac,2) == math.pow(ab,2)+math.pow(bc,2)):
            print("ABC la tam giac vuong")

else:
    print("Khong la tam giac")
