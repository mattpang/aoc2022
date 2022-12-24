lines = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''.split('\n')

import utils
# lines = utils.loadlines(24)
import networkx as nx
from collections import Counter

grid = dict()
m = dict()
snow = dict()
id=0
for y,line in enumerate(lines):
    if y>0 and y<len(lines):
        for x,c in enumerate(line):
            if c !='.' and c!='#':
                grid[(x,y)] = c
                snow[(x,y)] = True
                m[id] = [c,[x,y]]
                id+=1
# print(grid)
xs = 0
xmax = len(lines[0])
ys = 0 
ymax = len(lines)

start = (1,0)
end = (len(lines[0])-2,len(lines)-1)

def plus(a,b):
    return (a[0]+b[0],a[1]+b[1])

width = len(lines[0])
height = len(lines)

def render(grid,curr=(1,0)):
    values = set([tuple(x[1]) for x in grid.values()])
    lookup = {tuple(x[1]): x[0] for x in grid.values()}

    #print(lookup)

    for j in range(len(lines)):
        l = ''
        for i in range(len(lines[0])):
            if (i,j) in values:
                l+=lookup[(i,j)]
            # elif start == (i,j):
            #     l+='S'
            # elif end == (i,j):
            #     l+='O'
            elif curr == (i,j):
                l+='E'
            elif (j == 0) or (j == ymax-1) or i == 0 or i == xmax -1 :
                l+='#'
            else:
                l+='.'
        print(l)


moves = {'>':(1,0),'^':(0,-1),'v':(0,1),'<':(-1,0)}

blizzard = dict()
# simulate the blizzard first
blizzard[0] = m.copy()
snow_t = dict()
snow_t[0] = snow.copy()

# render(blizzard[0])
# exit()


for t in range(1,1000):
    blizzard[t] = m.copy()
    snow_t[t] = dict()

    for id,pos in blizzard[t-1].items():
        next_move = list(plus(pos[1],moves[pos[0]]))
        if next_move[0] == xmax-1:
            next_move[0] = 1
        elif next_move[0] == 0:
            next_move[0] = xmax-2

        if next_move[1] == ymax-1:
            next_move[1] = 1
        elif next_move[1] == 0:
            next_move[1] = ymax-2  

        nx = tuple(next_move)
        blizzard[t][id][1] = nx
        snow_t[t][nx] = True
    #render(blizzard[t])
    #print('')
    #blizzard[t+1]

print('done')
# precalulated all the blizzard positions. now find out how to travel through it.
# at each t, add all the possible moves to the next list.

def possible_moves(curr,nextsnow):
    # can move NSEW and stay.
    allowed = []
    for m in [(1,0),(0,-1),(0,1),(-1,0),(0,0)]:
        nx = plus(curr,m)
        # this blocks the end point from being reached
        if nx in [start,end]:
            if nx not in nextsnow:
                allowed.append(nx)
        elif nx[0] != 0 and nx[0]!=width and nx[1]!=0 and nx[1]!=height:
            if nx not in nextsnow:
                allowed.append(nx)
    return allowed

current = start
t=0
all_moves = set(possible_moves(current, nextsnow=snow_t[t]))
while True:
    newmoves = set()
    for n in all_moves:
        for h in possible_moves(n,snow_t[t]):
            newmoves.add(h)
    all_moves = newmoves
    if end in all_moves:
        print(t)
        break
    t+=1

# part 2.
t=0
for current,out in [[start,end],[end,start],[start,end]]:
    # print(current,out)
    all_moves = set(possible_moves(current, nextsnow=snow_t[t]))
    while True:
        newmoves = set()
        for n in all_moves:
            for h in possible_moves(n,snow_t[t]):
                newmoves.add(h)
        all_moves = newmoves
        if out in all_moves:
            # print(t)
            t+=1
            break
        t+=1
print(t-1)