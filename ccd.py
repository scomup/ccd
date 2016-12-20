from enum import Enum
import numpy as np
from dstar import dstar_planner
import matplotlib.pyplot as plt
from grid_map import grid_map

def update_v(rows,cols,map_data,v_data):
    for i in range(rows):
        for j in range(cols):
            v_data[i,j] = map_data[i][j].h                      

ROBOT_SIZE = 3

g = grid_map(100,100)
g.init_map()
g.update_weight(ROBOT_SIZE)
dstar = dstar_planner(g)
dstar.add_start(g.map_data[0][0])
dstar.init_plan()
v_data = np.zeros((100,100))
update_v(100,100,g.map_data,v_data)

fig,ax=plt.subplots()
ax.set_aspect('equal')
ax.pcolor(v_data,cmap=plt.cm.Reds,edgecolors='k')
#print v_data
plt.show()
