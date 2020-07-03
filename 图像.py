import matplotlib.pyplot as plt
import numpy as np

# image data 三行三列的数据
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.xticks(())
plt.yticks(())

# cmap='bone' 等价于 cmap=plt.cm.bone cmap(color map), lower换成upper会上下颠倒
# interpolation可以去下方链接调整不同效果
# https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
plt.imshow(a,interpolation='catrom',cmap='bone',origin='lower')
plt.colorbar() # colorbar 有shrink等参数,shrink=0.9会缩短bar的长度

plt.show()