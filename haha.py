import numpy as np
from pandas import DataFrame,Series

df = DataFrame(np.random.randn(3,3),index=['row1','row2','row3'],columns=['col1','col2','col3'])
print(df)

print()
print('---------------------')
print(df.col1)

print()
print(df['col1'])

print()
print(df.loc[:,'col1'])

print()
print(df.iloc[:,0])

print()
print('---------------------')
print(df[0:1])

print()
print(df.loc['row1',:])

print()
print(df.iloc[0,:])