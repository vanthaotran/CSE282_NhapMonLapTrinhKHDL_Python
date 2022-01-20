# Bài 1 trong file BT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# quá trình training
# a)
# đọc file csv
wine = pd.read_csv("winequality-red (1).csv", sep=";")
wine.head
# y = ax+b
x = wine.loc[:,['alcohol']].values
y = wine.loc[:,['quality']].values
print(x)
print(y)
# tạo mô hình hồi quy
clf = linear_model.LinearRegression()
clf.fit(x,y)
# xác định hệ số hồi quy
print(clf.coef_)
# xác định b_ xác định sai số hồi quy
print(clf.intercept_)
# xác định sai số mô hình
print(clf.score(x,y))
# đường hồi quy
print(f"Phương trình hồi quy: [quality]={clf.coef_}*[alcohol]+{clf.intercept_}")
# vẽ pt hồi quy giữa chất lượng rượu và alcohol
plt.plot(x,clf.predict(x))
plt.scatter(x,y,c='r')
plt.show()
# quá trình test -> chạy mô hình dự báo
while True:
    x1 = float(input("alcohol = "))
    if x1 <= 0:
        break
    print("quality", x1, ":",clf.predict([[x1]]))


#b)
x = wine.drop("quality",axis=1)
y = wine['quality'].values
# CHUẨN HOÁ DỮ LIỆU, chuẩn hoá x-> biến đổi ma trận x dưới dạng 1 công thức được chuẩn hoá
x = x.apply(lambda x: (x-np.mean(x))) / (np.max(x))-np.min(x)

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

