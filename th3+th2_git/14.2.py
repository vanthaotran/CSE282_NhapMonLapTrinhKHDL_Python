# Hãy tạo 1 file có tên là: <mã sinh viên>.txt (ví dụ sinh viên có mã sv là: 123
# thì file cần đọc là: 123.txt). Mỗi thông tin sau trên 1 dòng: Họ tên, mã sinh viên,
# giới tính, ngày sinh, quê quán, số điện thoại, Facebook). Đọc 1 file trên
# và in ra màn hình 5
# dòng cuối cùng. (yêu cầu sinh viên lấy theo đúng thông tin của mình)

l=[]
with open('1951061116.txt') as f:
  for line in f:
    l.append(line)

for i in range(len(l)-5, len(l) ):
  print(l[i])