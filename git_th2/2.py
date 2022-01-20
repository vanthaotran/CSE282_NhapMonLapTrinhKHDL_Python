# tao ra 1 tuple gom cac so nguyen to < 1000
# b1: tao list rong
# b2: tim cac so nguyen to < 1000
# b3: chuyen danh sach thanh tuple
L = [];
n =  1000;
for i in range (1, 101):
    count = 0;
    for j in range(2, 101//2+1):
        if(i%j==0):
            count = count + 1;
    if count == 0:
        L.append(i);

print(L);
# for i in range(2, n//2+1):
#     count = 0;
#     if i % 2 == 0:
#         count += 1;
#     if count == 0:
#         L.append(i);
# t = tuple(L)
# print(t);

# for i in range(2, 1001):
#     count = 0;
#     for i in range(i, n//2+1):
#         if (i%j==0):
#             count+= 1;
#     if count == 0:

# for i in range(2, 10001):