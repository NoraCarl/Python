import numpy as np
import pandas as pd

Data_csv = pd.read_csv('C:\\Users\\cora\\Desktop\\table.csv')
Data_csv.rename(columns={'School':'学校','Class':'班级','ID':'学生ID','Gender':'性别','Address':'地址',
                        'Height':'身高','Weight':'体重','Math':'数学成绩','Physics':'物理成绩'},inplace=True)
print(Data_csv.head())  #查看头数据
print(Data_csv.tail())  #查看尾数据
print(Data_csv['物理成绩'].nunique()) # nunique显示该字段里面有多少唯一值
print(Data_csv['物理成绩'].unique()) #unique显示该字段所有的唯一值
print(Data_csv['物理成绩'].count())  # 返回非缺失值元素的个数
print(Data_csv['物理成绩'].value_counts()) # 返回每个元素的频数(分组)
Data_csv.info()  #对内容进行记录统计 并显示Dtype类型
print(Data_csv.describe(percentiles=[.05,.25,.75,.95]))  # 统计数值型数据的各个统计量
# 第一个percentiles,这个参数可以设定数值型特征的统计量，默认是[.25, .5, .75],也就是返回25%，50%，75%数据量时的数字.但是这个可以修改的
print(Data_csv['数学成绩'].idxmax())  # 求最大元素的下标
print(Data_csv['数学成绩'].idxmin())  # 求最小元素的下标
print(Data_csv['数学成绩'].nlargest())  # 显示较大的元素
print(Data_csv['数学成绩'].nsmallest())  # 显示较小的元素