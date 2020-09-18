import numpy as np
import pandas as pd

Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv')
Data_csv.rename(columns={'School':'学校','Class':'班级','ID':'学生ID','Gender':'性别','Address':'地址',
                        'Height':'身高','Weight':'体重','Math':'数学成绩','Physics':'物理成绩'},inplace=True)
print(Data_csv.head())  #查看头数据
print(Data_csv.tail())  #查看尾数据
print(Data_csv['物理成绩'].nunique()) # nunique显示该字段里面有多少唯一值
print(Data_csv['物理成绩'].unique()) #unique显示该字段所有的唯一值