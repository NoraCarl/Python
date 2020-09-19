import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline 设置中文编码
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False
#条形图
Bar_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='条形图')


if __name__ == "__main__":
    # 设置数据为降序
    Jiangxu = Bar_chart.sort_values(by='利润')
    # 创建画布figsize长宽为14，7
    plt.figure(figsize=(14,7))
    #设置标题名字，字体大小，字体颜色等
    plt.title('全国各地区分公司盈利情况', fontsize=20,color='red')
    # barh 制作水平条形图
    plt.barh(Jiangxu['地区'],Jiangxu['利润'])
    # 采用for循环x表示下标y表示元素
    for x,y in enumerate(Jiangxu['利润'].values):
        # 用text向坐标轴添加文本 x,y浮动
        plt.text(y,x,'%.2f' %y,fontsize=10,color='red')
    # 设置X轴标题、文字大小、文字颜色
    plt.xlabel('地区',fontsize=15,color='dimgray')
    # 设置y轴标题、文字大小、文字颜色
    plt.ylabel('盈利情况',fontsize=15,color='dimgray')
    # 设置x轴当前刻度位置、颜色、大小
    plt.xticks(rotation=-30,color='red',fontsize=13)
    # 设置y轴当前刻度位置、颜色、大小
    plt.yticks(color='red',fontsize=13)
    # 显示
    plt.show()
