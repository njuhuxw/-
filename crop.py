import numpy as np

from PIL import Image


o_img=Image.open('hot1.png').convert('L')
print(o_img.width,o_img.height)
img=np.array(o_img)

index = np.where((img > 0) & (img < 255))
min_x = min(index[0])
max_x = max(index[0])
min_y = min(index[1])
max_y = max(index[1])
print(min_x,min_y,max_x,max_y)

o_img.crop((min_y, min_x, max_y, max_x)).show()