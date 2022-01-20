# Đề 25 câu 2
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
#a
df = pd.read_csv('tieu_duong.csv')
print(df)
# b chuẩn hoá
df1 = df.drop('Class', axis = 1)
dfNor = df1.apply(lambda a: (a-np.min(a))/(np.max(a)-np.min(a)))
print("Chuẩn hoá dữ liệu [0,1]")
print(dfNor)
#c hoi quy tuyen tinh glucose vs Age
x = df.loc[:,['glucose']].values
y = df.loc[:,['Age']].values
clf = linear_model.LinearRegression()
clf.fit(x,y)
print('He so hoi quy: ',clf.coef_)
print('Sai so hoi quy: ',clf.intercept_)
print('Sai so mo hinh: ',clf.score(x,y))
print(f"Phuong trinh hoi quy: [Age]={clf.coef_}*[glucose]+{clf.intercept_}")
plt.plot(x,clf.predict(x))
plt.scatter(x,y,c='r')
plt.title("BIỂU ĐỒ TƯƠNG QUAN GIỮA GLUCOSE VỚI AGE")
plt.xlabel("Glucose")
plt.ylabel("Age")
plt.show()
#test
while True:
  x1 = float(input("Glucose: "))
  if x1<0:
    break
  print("Age: ", x1, ": ",clf.predict([[x1]]))
#d hồi quy đa biến
x2 = df1.drop('Age',axis=1)
y2 = df1['Age'].values
x2 = x2.apply(lambda x : (x - np.mean(x)) / (np.max(x)-np.min(x)) )
clf2 = linear_model.LinearRegression()
clf2.fit(x2,y2)
print(clf2.coef_)
print(pd.DataFrame({"Name":x2, "Hesohoiquy":clf2.coef_}).sort_values(by="Hesohoiquy"))
print(clf2.intercept_)
print(clf2.score(x2,y2))
#e vẽ biểu đồ so sánh giữa các thuộc tính đã chuẩn hóa 
# dfNor.sort_values(by=['Time','glucose','Diastolic','Triceps','Serum','Body','Diabetes'])
# column = dfNor.columns.values
# # plt.plot(df1['Age'], dfNor[column])
# plt.plot(df1['Age'], dfNor.sort_values(by="Time"),label='Time')
# # plt.legend(loc=2)
# plt.xlabel('Age')
# plt.show()
for column in dfNor.drop('Age', axis=1):
    plt.plot(df1['Age'], dfNor[column], marker='', linewidth=1, alpha=0.9, label=column)
plt.legend(loc=2, ncol=2)
plt.title("Biểu Đồ So Sánh Dữ Liệu Đã Chuẩn Hoá", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Age")
plt.ylabel("Index")
plt.show()
