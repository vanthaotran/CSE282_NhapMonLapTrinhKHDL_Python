# Đề 29 câu 1
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
#a+b
df = pd.read_csv('DB.csv')
df_drop = df.drop('Socum',axis=1)
print(df)
#c
x = df["Socum"].values
print(x)
y = df["Kmean"].values
z = df["FCM"].values
e = df["SSFCM"].values
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,e)
plt.xlabel("Số cụm")
plt.title("Biểu đồ đường so sánh")
plt.legend(['Kmean', 'FCM', 'SSFCM'])
plt.show()
#d xuat
plt.savefig("onthi.png")
# e max
print('Gia tri lon nhat do do DB theo tung so cum.')
maxClus = df_drop.max(axis=1)
print(maxClus)
