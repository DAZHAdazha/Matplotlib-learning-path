import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X /float(n)) * np.random.uniform(0.5,1.0,n) # 从0.5-1.0产生n个随机值
Y2 = (1 - X /float(n)) * np.random.uniform(0.5,1.0,n) # 从0.5-1.0产生n个随机值

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white') # 用正代表向上
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white') # 用-代表向下

# 给上方柱状图加上数值, 用zip把每个x,y 输出到X与Y中
for x,y in zip(X,Y1):
    # 前两个值为text坐标, ha=horizontal alignment对齐方式,va=vertical alignment
    plt.text(x + 0.1,y, '%.2f' % y,ha='center',va='bottom')
# 给上方柱状图加上数值, 用zip把每个x,y 输出到X与Y中

for x,y in zip(X,Y2):
    # -0.05向下,top向上对齐，且y2为整数，使其变成负的坐标
    plt.text(x + 0.1,-y, '-%.2f' % y,ha='center',va='top')

plt.show()