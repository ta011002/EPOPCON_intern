import pandas as pd

df = pd.read_csv('../__data/salaries.csv')
df

print(df['Salary'])

print(df[['Name', 'Salary']])

print('Salary min :', df['Salary'].min())
print('Salary mean :', df['Salary'].mean())

ser_of_bool = df['Age'] > 30
print(ser_of_bool)

df[ser_of_bool]

df[df['Age'] > 30]

df['Age'].unique()

df.columns

df.info()

df.describe()

df.index

import numpy as np

mat = np.arange(0, 50).reshape(5, 10)
mat

df = pd.DataFrame(data=mat)
df

mat = np.arange(0, 10).reshape(5, 2)
df = pd.DataFrame(data=mat)
df

mat = np.arange(0, 10).reshape(5, 2)
df = pd.DataFrame(data=mat, columns=['A', 'B'])
df