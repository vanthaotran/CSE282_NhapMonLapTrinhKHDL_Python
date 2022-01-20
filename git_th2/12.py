# Tạo một tập hợp gồm các số nhập vào từ bàn phím (nhập trên 1 dòng, cách
# nhau bởi ký tự trống), tìm và in ra số phần tử của tập, giá trị lớn nhất và nhỏ nhất trong
# tập

s = input("Nhap: ").split();
count = 0;
numMin = max(s);
numMax = min(s);
for i in range(len(s)):
    count = count + 1;

print(count);
print(numMin, numMax);


