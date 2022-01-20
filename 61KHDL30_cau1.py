# Đề 30 câu 1
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics
# a b
a = pd.read_csv('tuyensinh.csv')
print(a)
# c ve
a_Nam = a['Nam'].values
xxx = [1,2,3,4,5]
x = np.arange(5)
a_CNTT = a['CNTT'].values
a_HTTT = a['HTTT'].values
a_CNPM = a['CNPM'].values
width=0.2
plt.bar(x-0.2,a_CNTT,width,color='cyan')
plt.bar(x,a_HTTT,width,color='orange')
plt.bar(x+0.2,a_CNPM,width,color='green')
plt.xticks(x,xxx)
plt.xlabel("Nam")
plt.ylabel("Nganh")
plt.legend(["CNTT", "HTTT", "CNPM"])
plt.show()
#d
D = {}
a_drop_Nam = a.drop('Nam',axis=1)
a_name_column = a_drop_Nam.columns.values
LMean = []
for i in a_name_column:
  x = statistics.mean(a_drop_Nam[i])
  LMean.append(x)
zip_iterator = zip(a_name_column,LMean)
D = dict(zip_iterator)
print(D)
# e
listSV = []
for i in a_name_column:
  listSV.append(sum(a_drop_Nam[i]))
print('List luu tong so sinh vien tu 2014-2018 tung nganh: ',listSV)
