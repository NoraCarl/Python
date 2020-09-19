import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 相关矩阵图 相关系数:绝对值1相关性越强 1指代完全正相关 0完全不相关
plt.style.use('seaborn-whitegrid')
sns.set_style('white')
#相关矩阵图
Matrix_diagram = pd.read_excel('C:\\Users\\cora\\Desktop\\可视化图表案例数据.xlsx',sheet_name='相关矩阵图')
mx_data = Matrix_diagram.corr(method='pearson')
np.zeros((11,11))
plt.figure(figsize=(16,12))
# 设置中文
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False
sns.heatmap(mx_data,
            xticklabels=mx_data.columns, #横坐标标签
            yticklabels=mx_data.columns, #纵坐标标签
            cmap='rainbow', #使用的光谱
            center=0, # 基准 越靠近两端的值 颜色月接近于对应的设定值
            annot=True
            )
plt.title('相关矩阵',fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.show()