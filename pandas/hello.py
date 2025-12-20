import numpy as np
import pandas as pd

# dict1 = {
#     "name":['aman','rahul','sachin','rohit'],
#     "age":[23,45,34,22],
#     "city":['delhi','mumbai','bangalore','chennai']
         
#         }

# df = pd.DataFrame(dict1)
# print(df)

# df.to_csv('mydata.csv',index=False)
#df.hed(2)
#df.tail(2)

# print(df.describe())

prem = pd.read_csv('pandas/prem.csv')
# prem['age'][0] = 90
# print(prem)
# print(prem['age'])

# print(prem['age'][0])

# prem.to_csv('pandas/prem.csv')
# prem.index = ['a','b','c','d']
# print(prem)
# ser = pd.Series(np.random.rand(34))
# print(ser)

newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newdf)
# print(newdf.describe())
# print(newdf.head())
# print(newdf.dtypes)
# newdf[0][0] = 'aman'
# print(newdf.dtypes)
# print(newdf.head())


# print(newdf.to_numpy())

# newdf[0][0] = 100
# print(newdf.head())

# print(newdf.T)
# newdf.sort_index(axis=0,ascending=False)
# print(newdf.sort_index(axis=1 ,ascending=False))
# print(newdf[0])

# newdf2 = newdf
# newdf2[0][0] = 9999
# print(newdf2.head())

# newdf2 = newdf.copy()
# newdf2[0][0] = 9999
# print(newdf2.head())
# print(newdf.head())
 
# newdf.loc[0,0] = 5555
# print(newdf.head())

newdf.columns = list('ABCDE')
print(newdf.head())

# newdf.loc[0,0] = 12345
# print(newdf.head(2))
# newdf = newdf.drop(0,axis=1)
# print(newdf.head(2))

# newdf = newdf.loc[[1,2],[ 'B','C']] 
# print(newdf.head())
 

# # newdf = newdf.loc[[1,2],:]
# newdf = newdf.loc[:,[ 'B','C']]
# print(newdf.head())

# print(newdf.loc[(newdf['A']<0.3)])
#print(newdf.loc[(newdf['A']<0.3 ) & (newdf['B']>0.5)])
# print(newdf.iloc[0,4])
# print(newdf.drop([0]))
# print(newdf.drop(['A','B'],axis=1))
# print(newdf.reset_index())
# newdf.loc[:,['A']] = 56
# newdf['A'].isnull()
print(newdf.head())