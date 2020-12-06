import numpy as np
from pandas import DataFrame,Series
print('------------------------')

df = DataFrame(np.arange(9).reshape([3,3]),index=['row1','row2','row3'],columns=['col1','col2','col3'])
print(df)

#添加一个新的列
print()
col4 = Series(['one','two','two'],index = ['row1','row2','row3'])#index 必须加 不然为NaN
df['col4'] = col4
print(df)

#过滤列col4中为two的行 输出col4中为two的行 
print()
print(df[df['col4'].isin(['two'])])

#过滤大于0的数 输出df其他为NaN
print()
print(df[df>5])

#过滤第一列大于3 输出该列中大于3所在的行
print()
print(df[df['col1']>2])

#过滤第一行大于0 输出df其他为NaN
print()
print(df[df[0:1]>0])

print()
print('-------------------------')
print(df)

print()
#df.iloc[0,0] = 'NaN' 令某个值等去NaN 只是等于一个字符串，并不是为缺失值
print(df[df[0:1]>=0].dropna(how = 'any'))#真正的缺失值才dropna有效

#对于某一行赋值，必须要有指定的长度，无法造成缺失值
print()
df[0:1]=[10,11,22,33]
print(df)

#对于某一列赋值，可以只设置几个index，剩下的index对应的值为缺失值
print()
df['col1']=Series([1010,22],index = ['row1','row2'])
print(df)
print()
print(df.dropna(how='any'))
