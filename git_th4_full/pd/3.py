import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = {
#     "soluongmau" : [300,500,700,1000,1200,1500,1800,2000],
#     "KNN" : [0.904, 0,893, 0.863, 0.823, 0.802, 0.783, 0.765, 0.752],
#     "FIS" : [0.912, 0.901, 0.863, 0.812, 0.794, 0.743, 0.732, 0.723]
# }
# df = pd.DataFrame(data)
# print(df)





# data = {
#         "soluongmau" : [300,500,700,1000,1200,1500,1800,2000],
#         "KNN" : [0.904, 0,893, 0.863, 0.823, 0.802, 0.783, 0.765, 0.752],
#         "FIS" : [0.912, 0.901, 0.863, 0.812, 0.794, 0.743, 0.732, 0.723]
# }
# df = pd.DataFrame(data)
# print(df)


# data = {
#     "soluongmau" : pd.Series([300,500,700,1000,1200,1500,1800,2000]),
#     "KNN" : pd.Series([0.904, 0,893, 0.863, 0.823, 0.802, 0.783, 0.765, 0.752]),
#     "FIS": pd.Series([0.912, 0.901, 0.863, 0.812, 0.794, 0.743, 0.732, 0.723])
# }
# df = pd.DataFrame(data)
# print(df)
# df.to_csv("K59.csv")


# BÀI 2 SLIDE, ghi thang data vao!
# import csv
# with open('k59.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["soluongmau", "knn", "fis"])
#     writer.writerow([300, 0.904, 0.912])
#     writer.writerow([500, 0.893, 0.901])
#     writer.writerow([700, 0.863, 0.863])
#     writer.writerow([1000, 0.823, 0.812])
#     writer.writerow([1200,0.802, 0.794])
#     writer.writerow([1500, 0.783, 0.743])
#     writer.writerow([1800, 0.765, 0.732])
#     writer.writerow([2000, 0.752, 0.723])
# df = pd.read_csv("k59.csv")
# print(df)
# x = df["knn"].values
# y = df["fis"].values
# plt.bar(x,y)
# plt.show()


# okay code!
df = pd.read_csv("K59.csv")
print(df)
df.KNN.plot(kind='bar', label='One')
df.FIS.plot(kind='bar', label='Two', color='g')
plt.legend()
plt.show()
plt.savefig('knnfis.png')






















