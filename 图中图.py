import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,9,4,2,3,5,6]

# 确定大图的位置
left, bottom, width, height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r') # red
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.5,0.6,0.25,0.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b') # blue
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('inside 9')

# 第二种方法生成图中图
plt.axes([.7,.2,.2,.2])
plt.plot(y[::-1],x,'g') # green
plt.xlabel('x')
plt.ylabel('y')
plt.title('inside 2')

plt.show()