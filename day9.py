from collections import Counter,defaultdict
import numpy as np

lines = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''.split('\n')[:-1]
import utils

lines = utils.loadlines(9)

def check(h,t):
    x=0
    y=0 

    if (abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1):
        x =  np.clip(h[0]-t[0],-1,1)
        y =  np.clip((h[1]-t[1]),-1,1)
    elif abs(h[0]-t[0]) > 1:
        x =  np.clip(h[0]-t[0],-1,1)
    elif abs(h[1]-t[1]) > 1:
        y =  np.clip((h[1]-t[1]),-1,1)
    #elif (abs(h[0]-t[0]) > 1) and (abs(h[1]-t[1]) == 0):

    return [x,y]

assert [0,0] == check([1,1],[0,0])
assert [1,0] == check([3,1],[1,1])
assert [0,1] == check([2,3],[2,1])
assert [1,-1] == check([2,1],[1,3])
assert [0,1] == check([1,3],[1,1])
assert [0,1] == check([1,3],[1,1])
assert [0,0] == check([3,3],[2,2])

def part1(lines):
    lookup = {'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1]}
    visited = Counter()
    hpos = [0,0]
    tpos = [0,0]
    visited[tuple(tpos)]+=1

    for line in lines:
        direction,amt = line.split(' ')
        amt = int(amt)
        for n in range(0,amt):
            hpos[0]+=lookup[direction][0]
            hpos[1]+=lookup[direction][1]
            # T must follow H if there's one unit away.
            tmove = check(hpos,tpos)
            tpos[0]+=tmove[0]
            tpos[1]+=tmove[1]
            visited[tuple(tpos)]+=1

    print(len(visited))
part1(lines)


def part2(lines):
    lookup = {'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1]}
    visited = Counter()
    
    knots = defaultdict(list)
    for i in range(0,10):
        knots[i] = [0,0]
    visited[tuple(knots[9])]+=1

    for line in lines:
        direction,amt = line.split(' ')
        amt = int(amt)
        for n in range(0,amt):
            knots[0][0]+=lookup[direction][0]
            knots[0][1]+=lookup[direction][1]
            # T must follow H if there's one unit away.
            for i in range(1,10):
                tmove = check(knots[i-1],knots[i])
                knots[i][0]+=tmove[0]
                knots[i][1]+=tmove[1]
            visited[tuple(knots[9])]+=1

    print(len(visited))

part2(lines)