lines = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.split('\n')
import utils
lines = utils.loadlines(18)
from collections import defaultdict,Counter
grid = Counter()
for line in lines:
    grid[tuple(map(int,line.split(',')))] = 1

total = 0 
faces = dict()
for g in grid.keys():
    for i in [-1,1]:
        if grid[(g[0]+i,g[1],g[2])]==0:
            total+=1
        if grid[(g[0],g[1]+i,g[2])]==0:
            total+=1
        if grid[(g[0],g[1],g[2]+i)]==0:
            total+=1
print(total)

# part 2 
# need to find pockets of air, so we minus that from total.
# a 1x1 airpocket is space which is filled at 6 sides by lava. 
# but maybe pocket can be different shape. 
# like part one but sort of the inverse.
from  skimage.segmentation import flood_fill

potential = []
xlist= []
ylist= [] 
zlist = []
for x,y,z in (grid.keys()):
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
    

def neighbours(x,y,z): 
    return [(x+dx, y+dy, z+dz) for (dx,dy,dz) in 
            [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]

import numpy as np
lava= np.zeros(shape=(max(xlist)+2,max(ylist)+2,max(zlist)+2))

for g in grid.keys():
    lava[g[0],g[1],g[2]] = 1

# print(lava[0,0,0])
# connectivity =1 exludes diagonals
ans = flood_fill(lava,(0,0,0),new_value=2,connectivity=1)
# print((ans==0).sum())
# print(np.product(lava.shape))

# then for each location, figure out the ext area of the airpockets
airpockets = Counter()
subtotal = 0
f = np.where(ans==0)
#print(f[0])
for x,y,z in zip(f[0],f[1],f[2]):
    #print(x,y,z)
    airpockets[(x,y,z)] = 1

# then just do it surface areas again with trapped pockets.
for g in airpockets.keys():
    for i in [-1,1]:
        if grid[(g[0]+i,g[1],g[2])]==1 and airpockets[(g[0]+i,g[1],g[2])]!=1:
            subtotal+=1
        if grid[(g[0],g[1]+i,g[2])]==1 and airpockets[(g[0],g[1]+i,g[2])]!=1:
            subtotal+=1
        if grid[(g[0],g[1],g[2]+i)]==1 and airpockets[(g[0],g[1],g[2]+i)]!=1:
            subtotal+=1

print(total-subtotal)
