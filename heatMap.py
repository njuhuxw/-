import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


file = np.load('hico9362.npy', 'r')
f = []

for i in range(640):
    s = []
    for j in range(436):
        s.append(file[i][j][6])
    f.append(s)

def draw_heatmap(data, map_name, vmin, vmax):
    cmap = cm.get_cmap('rainbow', 1000)
    h, w = len(data), len(data[0])
    figure = plt.figure(figsize=(int(w * 1.2 / 32), int(h * 1.2 / 32)))
    plt.figure(facecolor='w')
    ax = figure.add_subplot(111)
    # ax.set_yticks([])
    # ax.set_xticks([])

    ax.axis("off")
    map = ax.imshow(data, cmap=cmap, extent=None, aspect='equal', vmin=vmin, vmax=vmax, )
    print
    'type', type(map)
    # fig = plt.gcf()
    # cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    # plt.savefig(map_name, dpi=32,  bbox_inches='tight', pad_inches=0.0)
    plt.savefig(map_name, bbox_inches='tight', dpi=32)

    plt.show()


draw_heatmap(f,"test",10,1000)