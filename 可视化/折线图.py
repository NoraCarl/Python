import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus']=False
# 导入 折线图
Line_chart = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='折线图')

if __name__ == "__main__":
    # figure创建画布 figsize设置画布的长宽
    plt.figure(figsize=(12,6))
    # title 设置折线图的标题
    plt.title('各月销售展示',fontsize=20)
    plt.plot(Line_chart['月份'],Line_chart['销售额'],
             label='销售额',
             color='tomato',
             marker='o',
             markersize=6,
             linestyle=':',
             linewidth=1)
    plt.xlabel('时间',fontsize=15)
    plt.ylabel('销售额',fontsize=15)
    plt.xticks(color='red')
    plt.yticks(color='red')
    for x,y in enumerate(Line_chart['销售额'].values):
        plt.text(x-0.95,y,'%.2f' %y,fontsize=12,color='green')
    plt.show()