import matplotlib.pyplot as plt
import numpy as np

n = 1024 # 点的数量
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) # 颜色按公式生成

# s=size, c=color,用T会map到每个点上去,alpha=透明度
plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

# 隐藏ticks的值
plt.xticks(())
plt.yticks(())

plt.show()