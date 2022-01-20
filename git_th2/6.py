# nhap chuoi cac so nhi phan ngan cach boi dau ,
# in ra so thap phan
# chua lam duoc!

a = input().split(',');
b = [];
for i in a:
    c = 0;
    for j in i:
        c = c*2 + int(j);
    b.append(c);

print(b);