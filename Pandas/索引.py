import numpy as np
import pandas as pd

#index_col 用来指定表格的索引值
Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv',index_col='ID')
print(Data_csv.head(6))
'''
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
'''
#iloc 单行索引
print(Data_csv.iloc[2])
#iloc 多行索引
print(Data_csv.iloc[2:6])
#iloc 单列索引
print(Data_csv.iloc[:,4].head(3))
#iloc 多列索引
print(Data_csv.iloc[:,7::-2].head(3))
#iloc 综合索引
print(Data_csv.iloc[2:6:,7::-2].head(3))
#常用索引函数
#where函数 对条件为False的进行提取 通过以下的操作删除了单元格中不满足条件的行或提取出赛选后的新数组 
print(Data_csv.where(Data_csv['Gender']=='M').dropna().head())