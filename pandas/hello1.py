import pandas as pd
import numpy as np

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Batman',],
                        "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                        "born":[pd.NaT, pd. Timestamp ("1940-04-25"),
                        pd. NaT]})

print(df.head())
# print(df.dropna())
# print(df.dropna(how='all', axis=1 ))

# df.drop_duplicates(subset=['name'], keep='first', inplace=True)
# print(df)
#print(df['name'].value_counts(dropna=False))

print(df.notnull())