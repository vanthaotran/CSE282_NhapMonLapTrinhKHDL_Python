import pandas as pd
import numpy as np

iris = pd.read_csv("iris.csv")
print(iris)
# tim max, min, sum 1 cot
print(iris.max())
print(iris.min())
print("SUMMMM");
print(iris.sum())


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
# df.to_csv("K61.csv")