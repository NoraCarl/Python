import numpy as np
import pandas as pd

#index_col 用来指定表格的索引值
Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv',index_col='ID')
print(Data_csv.head(6))
#loc 单行索引
print(Data_csv.loc[1101])
#loc 多行索引 [[]]
print(Data_csv.loc[[1101,1103,1201]])
#loc 范围行索引
print(Data_csv.loc[1103:1203])
#loc 单列索引
print(Data_csv.loc[:,'Weight'].head())
#loc 多列索引
print(Data_csv.loc[:,['Address','Height','Math']].head())
#loc 综合索引
print(Data_csv.loc[1102:2301,['Address','Height','Math']])

#iloc