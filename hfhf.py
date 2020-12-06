import numpy as np
from pandas import DataFrame,Series
print('------------------------')

df = DataFrame(np.arange(9).reshape([3,3]),index=['row1','row2','row3'],columns=['col1','col2','col3'])
print(df)

print()
print(df.mean())

print()
print(df.mean(1))

print()
print(df.apply(lambda x:x.max()-x.min()))