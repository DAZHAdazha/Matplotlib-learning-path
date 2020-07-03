import matplotlib.pyplot as plt

# 创建窗口
plt.figure()

# 创建小图,2行1列位置的第1个, 将第一张图变大
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

# 创建小图,2行3列位置的第4个
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

# 创建小图,2行2列位置的第5个
plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

# 创建小图,2行2列位置的第6个
plt.subplot(2,3,6)
plt.plot([0,1],[0,4])

plt.show()