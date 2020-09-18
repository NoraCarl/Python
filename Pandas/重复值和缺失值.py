import numpy as np
import pandas as pd
'''
Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv',index_col='ID')
print(Data_csv.head())

# 索引排序 index
#ascending=False为降序 默认是升序
print(Data_csv.set_index('Weight').sort_index(ascending=False).head(6))

# 值排序 values
print(Data_csv.sort_values(by='Math',ascending=False).head(3))
# 多值排序 values
print(Data_csv.sort_values(by=['Math','Height'],ascending=False))

# 重复值
# duplicated 告诉我们是否重复以Boolean返回 第一次出现为False 之后重复可多次出现True
print(Data_csv.duplicated('Address'))
# drop_duplicates
# last 保留重复值中最后出现的 first保留重复值中第一次出现的
print(Data_csv.drop_duplicates('Class',keep='last')) # 保留删除重复值的唯一项
print(Data_csv.drop_duplicates(['School','Class'],keep = 'last'))  # 两则相同 则重复
'''

#缺失值
Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table_missing.csv')
print(Data_csv.head())
print(Data_csv.isna().sum())  # 查看每列多少缺失值
print(Data_csv[Data_csv['Weight'].isna()])  # 查看缺失值所在行
print(Data_csv[Data_csv.notna().all(1)]) # 选出所有缺失或则非缺失列
# 数据的填充或放置或删除
print(Data_csv['Physics'].fillna('banana'))  # 填充缺失值 需设置inplace=True才能更改原数据
print(Data_csv['Physics'].fillna(method='ffill')) # ffill 用上一行的值填充 backfill用下一行的值填充
print(Data_csv['Weight'].fillna(Data_csv['Weight'].mean()).head())  # 使用平均值、众值、中卫值
print(Data_csv.dropna(axis=1)) # axis=1如果又NaN列有空值 一列都会被删除
print(Data_csv.dropna(axis=0)) # axis=0如果有NaN行有空值 一行都会被删除