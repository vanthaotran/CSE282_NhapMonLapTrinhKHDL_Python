# tao list, dua day so fiboncci vao
n = int(input("Nhap n = "));
L = [0,1];
if n < 0:
    print("Khong co day so Fibinacci");
elif n == 0:
    print("[0]");
elif n == 1:
    print("[0,1]");
else:
    for i in range(2,n+1):
        L.append(L[i-2] + L[i-1]);

print(L);
