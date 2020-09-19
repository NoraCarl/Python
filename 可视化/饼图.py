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
    plt.pie(Pie_chart['全年销售额占比'],labels=Pie_chart['国内地区'],
            explode=[0.1,0.1,0.1,0.1,0.1,0.1],
            wedgeprops={'linewidth':1,'edgecolor':'dimgray'})
    plt.show()