# Đề 26 câu 2
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics, tree
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn
#a
a = pd.read_csv('winequality-red-fix.csv',sep=';')
# print(a)
df = a.drop('quality',axis=1)
print(df)
#b chuẩn hoá
dfNor = df.apply(lambda a: (a-np.min(a))/(np.max(a)-np.min(a)))
print(dfNor)
#c KNN
X = a.drop("quality", axis=1)
Y = a["quality"].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
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
# e Vẽ biểu đồ so sánh giữa các thuộc tính đã chuẩn hóa ?
for column in dfNor.drop('alcohol', axis=1):
    plt.plot(df['alcohol'], dfNor[column], marker='', linewidth=1, alpha=0.9, label=column)
plt.legend(loc=2, ncol=2)
plt.title("BIỂU ĐỒ SO SÁNH", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Alcohol")
plt.ylabel("Index")
plt.show()
