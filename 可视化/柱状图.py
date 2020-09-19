import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline 设置中文编码
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False

# 柱状图
Histogram = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='柱状图')

#四象限图
Quadrant_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='四象限图')
#饼图
Pie_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='饼图')

#组合图
Acd = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='组合图')


if __name__ == "__main__":
    Histogram.rename(columns={'数量':'成交总数'},inplace=True)
    plt.figure(figsize=(12,6),facecolor='azure') #gigsize创建长宽的画布 facecolor设置画布的底色
    plt.title("各产品推广情况",fontsize=30,color='red')  # 创建图标题 fontsize这是字体大小 color修改标题颜色
    plt.bar(Histogram['放款产品类型'],Histogram['成交总数'],alpha=0.5,width=0.5,color='cornflowerblue') # alpha可以设置透明度 width控制柱形图的宽度 color设置柱状图颜色
    for x,y in enumerate(Histogram['成交总数']):
        plt.text(x-0.22,y-0.2,'%d' %y,fontsize=14,color='red')
    plt.xlabel('成交类型',fontsize=20) # x轴标题
    plt.ylabel('成交总数',fontsize=20) # y轴标题
    plt.xticks(rotation=-30,color='royalblue') # x字段名rotation旋转角度
    plt.yticks(color='royalblue')
    plt.show()