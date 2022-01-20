# Đề 24 câu 2
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import statistics
#a
a = pd.read_csv('Heart.csv')
print(a)
df = a.drop('Class',axis=1)
# b do lech chuan
print("Do lech chuan giua cac cot.")
print(df.std())
#c 
columnNames = df.columns.values
print(columnNames)
L = []
for i in columnNames:
  x = round(statistics.mean(a[i]),3)
  L.append(x)
tu = tuple(L)
print('Tuple trung binh cong: ',tu)
# d kmeans
x = a.drop('Class',axis=1)
y = a['Class'].values
model = KMeans(n_clusters=3).fit(x)
print(model)
kq = model.predict(x)
print(kq)
print(metrics.confusion_matrix(y,kq))
print("Model's label:",model.labels_)
print("Cum/ cluster: ", model.cluster_centers_)
print("So lan xac dinh lai tam cum: ",model.n_iter_)
#e
a_sorted = a.sort_values(by = "RestBP")
plt.plot(a_sorted["RestBP"], a_sorted["Chol"], color = "blue")
plt.title("BIỂU ĐỒ SO SÁNH SỰ TƯƠNG QUAN ")
plt.xlabel("RestBP")
plt.ylabel("Chol")
plt.show()
