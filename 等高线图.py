import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function 计算高度值
    return (1 -x/2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# 等高线需要定义网格
X,Y = np.meshgrid(x,y)

# use plt.contourf to filling contours(等高线) 8为等高线一共有10个等级也就是10个圈（默认0为2个,所以8+2=10）
#  cmap为将高度对于颜色 也有plt.cm.hot
plt.contourf(X,Y,f(X,Y),8,alhpa=0.75,cmap=plt.cm.cool)

# use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)

# adding label inline为若为True 则等高线不会穿过数据
plt.clabel(C,inline=True,fontsize=10)

# 去掉ticks
plt.xticks(())
plt.yticks(())

plt.show()