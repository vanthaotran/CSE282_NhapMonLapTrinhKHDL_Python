# Đề 22 câu 2
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import statistics
#a
a = pd.read_csv('glass.csv')
print(a)
df = a.drop('Class',axis=1)
# b do lech chuan
print("Do lech chuan giua cac cot.")
print(df.std())
#c 
columnNames = df.columns.values
print(columnNames)
L = []
# print(statistics.mean(a.RI))
for i in columnNames:
  x = round(statistics.mean(a[i]),3)
  L.append(x)
tu = tuple(L)
print('Tuple trung binh cong: ',tu)
#d kmean
x = a.drop('Class',axis=1)
y = a['Class'].values
model = KMeans(n_clusters=4).fit(x)
print(model)
kq = model.predict(x)
print(kq)
print(metrics.confusion_matrix(y,kq))
print("Model's label:",model.labels_)
print("Cum/ cluster: ", model.cluster_centers_)
print("So lan xac dinh lai tam cum: ",model.n_iter_)
#e ve
a_sorted = a.sort_values(by = "Na")
plt.plot(a_sorted["Na"], a_sorted["Mg"], color = "blue")
plt.title("BIỂU ĐỒ SO SÁNH SỰ TƯƠNG QUAN ")
plt.xlabel("Na")
plt.ylabel("Mg")
plt.show()
