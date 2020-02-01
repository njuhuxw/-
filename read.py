import seaborn as sns
import numpy as np
import pandas as pd
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from pyheatmap.heatmap import HeatMap
import seaborn as sns

# file=np.load('COCO_train2014_000000001580.npy','r')
file = np.load('hico9362.npy', 'r')
# file=np.load('COCO_val2014_000000000294.npy','r')

f = []

for i in range(640):
    s = []
    for j in range(436):
        s.append(file[i][j][6])
    f.append(s)
# for i in range(502):
#     s = []
#     for j in range(640):
#         s.append(file[j][i][6])
#     f.append(s)
# hm = HeatMap(f)
# hm.clickmap(save_as="~/hit.png")
# hm.heatmap(save_as="~/heat.png")

# sns.heatmap(data=f, square=False, vmax=20, vmin=0, robust=True,cmap='rainbow')
# sns.heatmap(data=f, square=False, vmax=20, vmin=0, robust=False,cmap="hot")
# sns.heatmap(data=f, square=False, vmax=10, vmin=0, robust=False,cmap="OrRd",cbar=False)
# sns.set_style("whitegrid")  #背景风格
# cmap = sns.cubehelix_palette(256,start=2, rot=0)
# cmap = sns.light_palette("#980002", 256)
# cmap = sns.light_palette("#154406", 256)
# cmap = sns.light_palette("#c65102", 256)
# cmap = sns.light_palette("#011288", 256)
# cmap = sns.light_palette("#fd411e", 256)
# cmap = sns.light_palette("#06b48b", 256)
# cmap = sns.light_palette("#06b48b", 256)
# cmap=sns.cubehelix_palette(8,reverse=True)
# sns.palplot(cmap)
# cmap = sns.light_palette("black", 256)
sns.heatmap(data=f, square=False, vmax=7, vmin=1,cmap='hot',cbar=False)

# plt.title("test")
plt.axis('off')
# plt.xticks([])  #去掉横坐标值
# plt.yticks([])  #去掉纵坐标值
# plt.legend.remove()
# plt.legend(loc='best',frameon=False) #去掉图例边框
plt.savefig("hico9362-6.png")
plt.show()

im = cv2.imread("hico9362-6.png")
im_h, im_w = im.shape[:2]
im_resized = cv2.resize(im, (436, 640))
cv2.imwrite("hico9362-6-resize.png", im_resized)
