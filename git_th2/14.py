# Nhập một string S, hãy tạo từ điển D trong đó key là các chữ xuất hiện trong
# S còn value tương ứng là số lần xuất hiện các chữ đó trong S

D = {};
s = input("Nhap s = ");
a = len(s);
while a > 0:
    key = s[0];
    dem = 0;
    j = 0;
    while j < len(s):
        if s[j] == key:
            dem = dem + 1;
            s = s[0:j] + s[j+1:];
        else:
            j = j + 1;
    D[key] = dem;
    a = len(s);
print(D);