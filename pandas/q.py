import pandas as pd
import numpy as np

# df = pd.DataFrame({'a':[1,2,3,4],
#                    'b':[5,6,7,8]})
# print(df.head())
# print(df.describe())
# print(df.dtypes)
# print(df.mean())
# print(df.sum())
# print(df.std())
# print(df.min())
# print(df.max()) 
# print(df.median())
# print(df.count())
# print(df.corr())

data = pd.read_excel('pandas/DATA.xlsx')
print(data.head())
    