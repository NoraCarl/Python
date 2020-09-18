import numpy as np
import pandas as pd

Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv',index_col='ID')
print(Data_csv.head())
'''
# 索引排序 index
#ascending=False为降序 默认是升序
print(Data_csv.set_index('Weight').sort_index(ascending=False).head(6))

# 值排序 values
print(Data_csv.sort_values(by='Math',ascending=False).head(3))
# 多值排序 values
print(Data_csv.sort_values(by=['Math','Height'],ascending=False))
'''
# 重复值
# duplicated 告诉我们是否重复以Boolean返回 第一次出现为False 之后重复可多次出现True
print(Data_csv.duplicated('Address'))
# drop_duplicates
# last 保留重复值中最后出现的 first保留重复值中第一次出现的
print(Data_csv.drop_duplicates('Class',keep='last')) # 保留删除重复值的唯一项
print(Data_csv.drop_duplicates(['School','Class'],keep = 'last'))  # 两则相同 则重复
