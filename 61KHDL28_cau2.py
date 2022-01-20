# Đề 28 câu 2
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
import sklearn
#a
a = pd.read_csv('Iris.csv')
print(a)
df = a.drop('class',axis=1)
print(df)
#b
dfNor = df.apply(lambda a: (a-np.min(a))/(np.max(a)-np.min(a)))
print(dfNor)
# c KNN
X = a.drop("class", axis=1)
Y = a["class"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)
model1 = KNeighborsClassifier()
model1.fit(X_train, Y_train)
result1 = model1.predict(X_test)
print("score:", model1.score(X_test, Y_test))
print("KNN: ")
print(result1)
print("Ma trận tương quan")
print(metrics.confusion_matrix(Y_test, result1))
print(metrics.classification_report(Y_test, result1))
# d
model2 = tree.DecisionTreeClassifier()
model2.fit(X_train, Y_train)
result2 = model2.predict(X_test)
print("Score:", model2.score(X_test, Y_test))
print("TREE: ")
print(result2)
print("Ma trận tương quan")
print(metrics.confusion_matrix(Y_test, result2))
print(metrics.classification_report(Y_test, result2))
#e ??? not sure
# mean of 4 columns---bar
# meanListChart = []
# dfNameColumn = df.columns.values
# for i in dfNameColumn:
#   meanListChart.append(df[i].mean())
# print(dfNameColumn)
# print(meanListChart)
# # so sanh gia tri giua cac nhom khac nhau! (mean)
# plt.bar(dfNameColumn, meanListChart)
# plt.plot(dfNameColumn, meanListChart, marker='o', markersize=10, linestyle='-.')
# plt.show()------------bar
df.plot.line(title="Biểu Đồ So Sánh")
plt.show()
