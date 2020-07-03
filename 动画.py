import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax = plt.subplots()

# sin图像
x= np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x)) # 返回是个列表，只接受第一位即可

# 定义改变的动画
def animate(i): # 传入第i帧
    line.set_ydata(np.sin(x + i / 10)) # 改变y的值
    return line,

# 定义起始动画
def init():
    line.set_ydata(np.sin(x))
    return line,


# frames 每次100帧 blit传入boolean,若true只更新变动的点,mac貌似只能用false,
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=True)

plt.show()