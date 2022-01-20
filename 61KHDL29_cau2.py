# Đề 29 câu 2
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import statistics
#a
a = pd.read_csv('Iris.csv')
y = a['class'].values
print(a)
df = a.drop('class',axis=1)
#b
L = []
column_name = df.columns.values 
for i in column_name:
  a = np.power(df[i].values,2)
  L.append(round(sum(a),4))
print('Tong binh phuong cua gia tri cac thuoc tinh: ',L)
#c
LTuple = []
for i in column_name:
  x = round(statistics.mean(df[i]),3)
  LTuple.append(x)
tu = tuple(LTuple)
print('Tuple trung binh cong: ',tu)
#d vẽ
newDfDrawing = df.drop(['petallength', 'petalwidth'],axis=1)
newDfDrawing.plot.line(title="Biểu Đồ Tương Quan")
plt.show()
# e kmean
x = df
model = KMeans(n_clusters=5).fit(x)
print(model)
kq = model.predict(x)
print(kq)
print(metrics.confusion_matrix(y,kq))
print("Model's label:",model.labels_)
print("Cum/ cluster: ", model.cluster_centers_)
print("So lan xac dinh lai tam cum: ",model.n_iter_)
