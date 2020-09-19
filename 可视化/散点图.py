import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt

#设置中文
plt.rcParams['font.sans-serif']=['Simhei']
plt.rcParams['axes.unicode_minus']=False

# 设置随机值
N = 10000
x = np.random.randn(N)
y = np.random.randn(N)


if __name__ == "__main__":
    plt.figure(figsize=(12,6))
    plt.scatter(x, y,s=100,alpha=0.5,edgecolors= 'white')
    plt.title('complex',fontsize=30)#显示图表标题
    plt.xlabel('这里是x轴')#x轴名称
    plt.ylabel('这里是y轴')#y轴名称
    plt.grid(False)#显示网格线
    plt.show()