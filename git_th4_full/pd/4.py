import pandas as pd
import numpy as np

data = {
    "MaNT" : pd.Series(['AUD','CAD','CHF','EUR','GBP','HKD','JPY','SGD','THB','USD']),
    "MuaPM" : pd.Series([16.815,17.138,22.568,26.172,29.876,2.864,201,16.734,692,22.775])
}
df = pd.DataFrame(data)
#print(df.T)

# df = pd.read_csv("tigia.csv")
# print(df)
a = df.sort_values("MaNT", ascending=False)
df['VND'] = 300
# em khong biet lam cau d a!
print(df)