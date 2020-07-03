import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 定义图像的窗口
fig = plt.figure()
# 给窗口加上3D的轴
ax = Axes3D(fig)

# 填数据
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
# 把X,Y 映射到地面
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X ** 2 + Y ** 2)
# height value 生成高度值
Z = np.cos(R)

# cstride= column stride, rstride = row stride, 指3d图每一格的跨度
ax.plot_surface(X,Y,Z,rstride=2,cstride=2,cmap=plt.get_cmap('rainbow'),edgecolor='white')

# 下方 等高线的图, zdir='z为从z轴压下等高图
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()