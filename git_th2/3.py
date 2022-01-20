# nhap chuoi, kiem tra co phai email khong
# b1: nhap chuoi
# b2: ktra isEmail?


s = input("Nhap chuoi s = ");
a = len(s);
count = 0;
for i in range(len(s)):
    if(s[i] == '@'):
        count += 1;

if count == 1:
    print("La email");
else:
    print("Khong la email");