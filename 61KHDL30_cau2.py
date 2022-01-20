# Đề 30 câu 2
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import io
#a
a = pd.read_csv('winequality-red-fix.csv',sep=';')
print(a)
#b
df = a.drop('quality',axis=1)
dfNor = df.apply(lambda a: (a-np.min(a))/(np.max(a)-np.min(a)))
print(dfNor)
# c citric acid vs quality
x = a.loc[:,['citric acid']].values
y = a.loc[:,['quality']].values
clf = linear_model.LinearRegression()
clf.fit(x,y)
print("he so hoi quy", clf.coef_)
print("sai so hoi quy", clf.intercept_)
print("sai so mo hinh", clf.score(x,y))
print(f"Phương trình hồi quy: [quality]={clf.coef_}*[citric acid]+{clf.intercept_}")
plt.plot(x, clf.predict(x))
plt.scatter(x,y,c='r') # show diem
plt.title("BIỂU ĐỒ TƯƠNG QUAN GIỮA CITRIC ACID VỚI QUALITY")
plt.xlabel("Citric acid")
plt.ylabel("Quality")
plt.show()
#test
while True:
  x1 = float(input("citric acid]: "))
  if x1 < 0:
    break
  print('quality: ', x1, ":", clf.predict([[x1]]))
# d ...vs quality
x2 = dfNor
y2 = a['quality'].values
clf2 = linear_model.LinearRegression()
clf2.fit(x2,y2)
dt = {
    "Name" : x2,
    "He so hoi quy" : clf2.coef_
}
print(pd.DataFrame(dt).sort_values(by="He so hoi quy") )
print("sai so hoi quy", clf2.intercept_)
print("sai so mo hinh", clf2.score(x2,y2))
# e Vẽ biểu đồ so sánh giữa các thuộc tính đã chuẩn hóa ???
for column in dfNor.drop('alcohol', axis=1):
    plt.plot(df['alcohol'], dfNor[column], marker='', linewidth=1, alpha=0.9, label=column)
plt.legend(loc=2, ncol=2)
plt.title("BIỂU ĐỒ SO SÁNH", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("alcohol")
plt.ylabel("Index")
plt.show()
