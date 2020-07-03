import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50) # -1到1的50个数据
y1 = 2 * x + 1 # 一次函数
y2 = x ** 2  # 二次函数

# 可以显示多张图片 用一次figure()则下面的代码会作用于该图片
plt.figure()
plt.plot(x,y1) # 画图

#第二张图
plt.figure(num=3, figsize=(8,5))  # 若不给num参数则默认为figure1,figure2,figure3顺序排列 figsize来确定figure长宽
# 设置图例(legend)
l1, = plt.plot(x,y2,label='up') # 先使用label给线设置名字 注意要想传到handles里面需要给线条对象加逗号！！！
# plt 两条线 并对第二条线设置样式,以及label名字
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[l1,l2],loc='best') # 显示设置的图例 handles 'best'指自动找一个空的位置，也可改为'upper right'等位置

# 设置坐标轴
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('this is x axis') # x轴描述
plt.ylabel('this is x axis') # y轴描述

new_ticks = np.linspace(-1,2,5)
# 设置x,y轴的每一格代表的值
plt.xticks(new_ticks)
# 数字形式字体用"r$xxx$"的格式,若有空格则应该用转义e.g. 'Jon Snow' => r'$Jon\ Snow$', \alpha可以打出alpha的字符形式
plt.yticks([-2,-1,0,1,2],
            [r'$awful$',r'$bad\ \alpha$','normal','good','great'])

# 移动坐标轴
# gca='get current axis'
ax = plt.gca()
# spines 是图四周的框
ax.spines['right'].set_color('none') # 清除右边的框
ax.spines['top'].set_color('none') # 清除上边的框
ax.xaxis.set_ticks_position('bottom') #把x轴设为bottom
ax.yaxis.set_ticks_position('left')  #把y轴设为left
ax.spines['bottom'].set_position(('data','0')) # 数据0时是y原点 # 其他参数 outward,axes
ax.spines['left'].set_position(('data','0'))# 数据0时是x原点

# 增加注解annotation
# 原直线中x=0.5的点
x0 = 0.5
y0 = 2 * x0 + 1
plt.scatter(x0,y0,s=50,color='b') # scatter为“点线”形式, 为原直线添加一个点,s为size,b=blue
plt.plot([x0,x0],[y0,0],'k--',lw=2.5) # 两个点确定一条直线,k=black,--=虚线,lw=linewidth

# method 1 to add annotation
# 第一个参数为text内容,xy为坐标,xycoords是指坐标基于data,xytext是相对x0y0点 x轴正30,y轴负30 textcoords是基于x0y0的点
# 字体16 arrowprops传入一个字典给出参数,arrowstyle为箭头样式，connectionstyle给出箭头的弧度,半径等
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# method 2 to add text(annotation)
plt.text(0.5,-1,r'$This\ is\ some\ text.\mu\ \sigma_i\ \alpha_t$',
fontdict={'size':16,'color':'r'}) # x=0.5,y=-1, r= red \sigma_i 指σ加角标i

# 设置tick的可见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # facecolor为前景色 alpha为透明度
    label.set_bbox(dict(facecolor='white',edgecolor='purple',alpha=0.7))

plt.show() # 出图