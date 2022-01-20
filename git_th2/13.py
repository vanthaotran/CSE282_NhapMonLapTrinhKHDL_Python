# Nhập một từ điển D có các value là các số nguyên, hãy in ra màn hình 3 giá
# trị value lớn nhất

D = {};
L = [];
listMax = [];
print("Nhap tu dien ");
yesNo = 'c';

while yesNo == 'c':
    key = input("Nhap key: ");
    value = int(input("Nhap value: "));
    L.append(value);
    D[key] = value;

    for j in range(0, 3):
        print(max(L));
        listMax.append(max(L));
        L.remove(max(L));

    yesNo = input('c/k: ');

print(max(L));