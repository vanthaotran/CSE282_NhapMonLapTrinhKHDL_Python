import pandas as pd
import numpy as np
#Series: cau truc 1 chieu, mang DL dong nhat

# S = pd.Series(np.random.randint(100, size=4))
# print(S)
# print(S.index)
# print(S.values)

# def Tang(x):
#     return x if x>500 else x+1000
# chi_so = ["Ke toan", "KT", "CNTT", "Co Khi"]
# gia_tri = [310,360,580, 340]
# S = pd.Series(gia_tri, chi_so)
# print(S.apply(Tang))

# dataframe: 2 chieu
# my_df = pd.read_csv("cpu.csv")
# print(my_df)

# names = [['MIT',1],['Standford',2],['DHTL',200]]
# df = pd.DataFrame(names)
# print(df)

# names = ["MIT", "DHTL", "Standford"]
# df = pd.DataFrame(names)
# print(df)

# crimes_rate = {
#     "Year" : [1960, 1961, 1962, 1963, 1964],
#     "Population" : [2312312,2443253,56464,232321,354532],
#     "Total" : [213213,432423452,436474,342342,4522],
#     "Violent" : [23123,2,432,423,423]
# }
# crimes_dataframe = pd.DataFrame(crimes_rate)
# print(crimes_dataframe)

# data = [
#     {
#         'MIT':500,
#         'Standford':4500,
#         'DHTL':15000
#     },
#     {
#         'MIT':1,
#         'Standford':23,
#         'DHTL':42
#     }
# ]
# df = pd.DataFrame(data, index=['NumOfStudents', "ranking"])
# print(df)

# data = {
#     "one":pd.Series([1,23,45], index=[1,2,3]),
#     "two":pd.Series([1000,2400,32321,2132], index=[1,2,3,4,])
# }
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("cpu.csv", index_col=0)
# df["SumVan"] = df["MMIN"] + df["CACH"] # them cot
# print(df.drop(["SumVan"], axis=1)) # xoa cot
# print("Tinh tong cot sumvan:") # tong cua cac cot
# print(df.SumVan.sum())
# print("Tinh tong tich luy cot sumvan: ") # tong trong qua trinh cong
# print(df.SumVan.cumsum())

