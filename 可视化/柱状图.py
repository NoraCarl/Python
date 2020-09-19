import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False

# 柱状图
Histogram = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='柱状图')
#条形图
Bar_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='条形图')
#折线图
Line_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='折线图')
#四象限图
Quadrant_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='四象限图')
#饼图
Pie_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='饼图')
#相关矩阵图
Matrix_diagram = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='相关矩阵图')
#组合图
Acd = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='组合图')

print(Histogram.info())