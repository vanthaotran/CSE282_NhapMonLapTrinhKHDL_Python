# nhap so n, in ra man hinh so nguyen duong < n co tong uoc so > chinh no

n = int(input("Nhap so n = "));
i = 1;
sum = 0;
L = [];
while i < n:
    if n%i == 0:
        sum += i;
    i = i + 1;

if sum > n:
    L.append(sum);

print(L);
