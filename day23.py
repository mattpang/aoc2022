lines = '''..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............'''.split('\n')

# lines = '''.....
# ..##.
# ..#..
# .....
# ..##.
# .....'''.split('\n')

from utils import loadlines
lines = loadlines(23)
from collections import Counter, namedtuple

w = len(lines[0])
h = len(lines)
grid = dict()
elf_moves = Counter()
elf_id = 0 
for y,line in enumerate(lines):
    for x,c in enumerate(line): 
        if c == '#':
            grid[elf_id] = (x,y)
            elf_moves[elf_id] = 0
            elf_id+=1


def t_add(a,b):
    return (a[0]+b[0],a[1]+b[1])

moves = (((0,-1),[(-1,-1),(0,-1),(1,-1)],'N'),#north
((0,1),[(-1,1),(0,1),(1,1)],'S'),#south
((-1,0),[(-1,-1),(-1,0),(-1,1)],'W'),#west
((1,0),[(1,-1),(1,0),(1,1)],'E'),#east
)
# each elf keeps a tracker of their move list. 

def check_neighbour(grid,pos,cur_pos):
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if i==0 and j==0:
                continue
            if t_add(pos, (i,j)) in cur_pos:
                return True
    return False


# print(grid.values())
mcount=0
m=0
part2 = True
while True:
# for part 1:
# for m in range(10):
    #print(m)
    if not part2:
        if m==10:
            break
    proposed_move = dict()
    # set sped things by up a factor of 3. 
    cur_pos = set(grid.values())
    # for id in elf_moves.keys():
        # elf_moves[id] = m

    for id,pos in grid.items():
        # check no elves nearby.
        # print('s',id,pos)
        neighbours = check_neighbour(grid,pos,cur_pos)

        if neighbours:
            # print('n',id,pos)
            for d in range(m,m+4):
                # Let's cycle through the moves. 
                # check each one. 
                my = moves[d%4]

                if (t_add(pos,my[1][0]) not in cur_pos) and (t_add(pos,my[1][1]) not in cur_pos) and (t_add(pos,my[1][2]) not in cur_pos) :

                    proposed_move[id] = t_add(pos,my[0])
                    break
                    
    # print(m,len(proposed_move))
    # second half
    #if the proposed_move is unique, allow. Otherwise both stay. 
    for id in proposed_move.keys():
        if list(proposed_move.values()).count(proposed_move[id])==1:
            # make the move
            grid[id] = proposed_move[id]
    
    if len(proposed_move) == 0:
        print('part2', m+1)
        break

    m+=1

x = []
y = []
for g in grid.values():
    x.append(g[0])
    y.append(g[1])g

area = (max(x)+1-min(x))*(max(y)+1-min(y))
# print(area)
if not part2:
    print('part 1:',area - len(grid))

# part 2
# when does it stop changing
