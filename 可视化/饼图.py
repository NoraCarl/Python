import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False
# 导入饼图
Pie_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='饼图')

if __name__ == "__main__":
    plt.figure(figsize=(10,5))
    plt.title('全国各地销售额占比情况',fontsize=20,color='red')
    # explode 控制每个扇面的数据
    plt.pie(Pie_chart['全年销售额占比'],
            #
            labels=Pie_chart['国内地区'],
            # explode 控制每个扇面的间距 数值越大间距越大
            explode=[0.1,0.1,0.1,0.1,0.1,0.1],
            # wedgeprops 对扇面的边框线设置
            wedgeprops={'linewidth':1,'edgecolor':'dimgray'},
            # colors 设置每个扇区的颜色
            colors=['red','green','peru','gold','turquoise','cyan'],
            # textprops 设置标签格式
            textprops={'fontsize':12},
            # autopct 显示数据标签百分比
            autopct='%.2f%%')
    # legend 添加图例
    plt.legend(Pie_chart['国内地区'],
               # title 设置标题
               title='地区',
               # fontsize 设置字体大小
               fontsize=12,
               # loc 设置位置
               loc='center left',
               # bbox_to_anchor 设置外边距、上、下等
               bbox_to_anchor=(1.2,0,0.5,1))
    plt.show()