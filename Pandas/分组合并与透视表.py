import numpy as np
import pandas as pd


Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv')
'''
# 单列分组
danlie = Data_csv.groupby('School')
print(danlie.sum())
#多列分组
duofen = Data_csv.groupby(['School','Class'])
print(duofen.sum())
#指定显示字段和指定分组的列
tiqu = Data_csv['Address Math'.split()].groupby('Address')
print(tiqu.count())


# 合并 merge  晚上多多尝试
sheet = pd.ExcelFile('C:\\Users\\cora\\Desktop\\用户借款数据.xlsx')
#print(sheet.sheet_names)
hb1 = pd.read_excel('C:\\Users\\cora\\Desktop\\用户借款数据.xlsx',sheet_name='基础信息')
hb2 = pd.read_excel('C:\\Users\\cora\\Desktop\\用户借款数据.xlsx',sheet_name='就业信息')
hb3 = pd.read_excel('C:\\Users\\cora\\Desktop\\用户借款数据.xlsx',sheet_name='借款信息')
data_two = pd.merge(hb1,hb2,how='outer')
print(data_two)
'''

# 透视表 pivot_table 通过不同的维度去展示数据
print(pd.pivot_table(Data_csv,index='Gender',columns='School',values='Height',aggfunc='mean'))