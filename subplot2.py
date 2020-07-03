import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1 : subplot2grid
"""
plt.figure()
# 共3行3列，从0,0开始,第一张图col为3，row为1,默认为1
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
# 注意子图设置方法在此时会变化
ax1.set_title('ax1')

ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)

ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)

ax4 = plt.subplot2grid((3,3),(2,0))

ax5 = plt.subplot2grid((3,3),(2,1))
"""
# method 2 : gridspec
"""
plt.figure()
# gs 为一个GirdSpec对象
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])
"""

# method 3: easy to define structure
"""
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
"""

plt.tight_layout()
plt.show()