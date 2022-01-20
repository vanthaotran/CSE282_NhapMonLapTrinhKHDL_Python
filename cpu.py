import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

# doc csv
df = pd.read_csv("cpu.csv")
# #y = ax+b
# x = df.loc[:, ['CHMAX']].values
# y = df.loc[:,['class']].values
# print(x)
# print(y)
# # tao mo hinh hoi quy
# clf = linear_model.LinearRegression()
# clf.fit(x,y)
# # he so hoi quy
# print(clf.coef_)
# # b, sai so hoi quy
# print(clf.intercept_)
# # sai so mo hinh
# print(clf.score(x,y))
# # duong hoi quy
# print(f"Phương trình hồi quy: [class]={clf.coef_}*[CHMAX]+{clf.intercept_}")
# # pt hoi quy giua CHMAX va class
# plt.plot(x,clf.predict(x))
# plt.scatter(x,y,c='r')
# plt.show()
# while True:
#     x1 = float(input("CHMAX = "))
#     if x1 <= 0:
#         break
#     print("class", x1, ":",clf.predict([[x1]]))

# đa thường không vẽ đồ

# hồi quy đa biến
x = df.drop("class",axis=1) # lấy tất cả
y = df['class'].values
# CHUẨN HOÁ DỮ LIỆU, chuẩn hoá x-> biến đổi ma trận x dưới dạng 1 công thức được chuẩn hoá
x = x.apply(lambda x: (x-np.mean(x)) / (np.max(x)-np.min(x)))
print(x)
print(y)
# tạo mô hình hồi quy
clf = linear_model.LinearRegression()
clf.fit(x,y)
# xác định hệ số hồi quy
print(clf.coef_)
print(pd.DataFrame({"Name":x, "Hesohoiquy":clf.coef_}).sort_values(by="Hesohoiquy"))
# xác định b_ xác định sai số hồi quy
print(clf.intercept_)
# xác định sai số mô hình
print(clf.score(x,y))