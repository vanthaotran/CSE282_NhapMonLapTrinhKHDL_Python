# Đề 23 câu 2
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
import sklearn
#a
a = pd.read_csv("Heart.csv")
print(a)
#b
print(a.std()) # độ lệch chuẩn
#c KNN
X = a.drop("Class", axis=1)
Y = a["Class"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
model1 = KNeighborsClassifier()
model1.fit(X_train, Y_train)
result1 = model1.predict(X_test)
print("score:", model1.score(X_test, Y_test))
print("KNN: ")
print(result1)
print("Ma trận tương quan")
print(metrics.confusion_matrix(Y_test, result1))
print(metrics.classification_report(Y_test, result1))
# d tree decision
model2 = tree.DecisionTreeClassifier()
model2.fit(X_train, Y_train)
result2 = model2.predict(X_test)
print("score:", model2.score(X_test, Y_test))
print("TREE: ")
print(result2)
print("Ma trận tương quan")
print(metrics.confusion_matrix(Y_test, result2))
print(metrics.classification_report(Y_test, result2))
# e ve bieu do
a_sorted = a.sort_values(by = "RestBP")
plt.plot(a_sorted["RestBP"], a_sorted["Chol"], color = "blue")
plt.title("BIỂU ĐỒ SO SÁNH SỰ TƯƠNG QUAN ")
plt.xlabel("RestBP")
plt.ylabel("Chol")
plt.show()
