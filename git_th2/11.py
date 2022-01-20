# Nhập một từ điển D, hãy in ra các value khác nhau trong từ điển
# value in ra khong duoc trung nhau

D = {};
# s = ();
L = [];
print("Nhap tu dien ");
yesNo = 'c';
while yesNo == 'c':
    key = input("Nhap key: ");
    value = input("Nhap value: ");
    L.append(value);
    D[key] = value;
    yesNo = input('c/k: ');

s = set(L);
print(s);