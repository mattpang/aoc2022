from string import ascii_lowercase
cmap = dict(zip(ascii_lowercase,range(len(ascii_lowercase))))
cmap['S'] = 0
cmap['E'] = 25
def check(p1,p2):
    if (cmap[p2]-cmap[p1])<=1:
        return True
    else:
        return False
# print(check("a","b"))
# print(check("a","c"))
# print(check("c","a"))
# print(check("b","z"))

# exit()
lines = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split('\n')
import utils
lines = utils.loadlines(12)

#print(lines)
import networkx as nx
grid = []
for line in lines:
    row = [x for x in line]
    grid.append(row)
# print(grid)

g = nx.DiGraph()
ymax = len(grid)
xmax = len(row)
alist = []
for y,row in enumerate(grid):
    for x,col in enumerate(row):
        if grid[y][x] == 'S':
            S = (y,x)
        if grid[y][x] == 'a':
            alist.append((y,x))

        if grid[y][x] == 'E':
            E = (y,x)
        
        if x>0 and x<xmax-1:
            for i in [-1,1]:
                if check(grid[y][x],grid[y][x+i]):
                    g.add_edge((y,x),(y,x+i))
        elif x==0:
            for i in [1]:
                if check(grid[y][x],grid[y][x+i]):
                    g.add_edge((y,x),(y,x+i))
        elif x==xmax-1:
            for i in [-1]:
                if check(grid[y][x],grid[y][x+i]):
                    g.add_edge((y,x),(y,x+i))

        if y>0 and y<ymax-1:
            for j in [-1,1]:
                if check(grid[y][x],grid[y+j][x]):
                    g.add_edge((y,x),(y+j,x))
        if y==0:
            for j in [1]:
                if check(grid[y][x],grid[y+j][x]):
                    g.add_edge((y,x),(y+j,x))
        if y==ymax-1:
            for j in [-1]:
                if check(grid[y][x],grid[y+j][x]):
                    g.add_edge((y,x),(y+j,x))
                

print(nx.shortest_path_length(g,S,E))
#print(nx.shortest_path(g,S,E))

#part2
ans = []
for ap in alist:
    try:
        ans.append(nx.shortest_path_length(g,ap,E))
    except:
        pass
print(min(ans))
