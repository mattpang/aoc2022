import numpy as np
import utils
lines = utils.loadlines(8)
rows = [] 

for line in lines:
    rows.append(list(map(int,list(line))))

grid = np.asarray(rows)

def vis(g):
    w,h = g.shape
    edge = 2*w+2*(h-2)
    #print(w,h,edge)
    # calc inner vis
    seen = np.zeros_like(g)
    for y in range(1,len(g)-1):
        for x in range(1,len(g[0])-1):
            #print(x,y)
            #check if this tree is blocked hoz and vis, if not we can add a plus 1
            #for each direction, check if its the highest to that edge
            # N,S,W,E
            # left, right, top, bottom
            #print(x,y,g[x,y],g[0:x,y],g[x:,y],g[x,0:y],g[x,y+1:])
            if ((g[x,y] > g[0:x,y]).all()) or ((g[x,y] > g[x+1:,y]).all()) or ((g[x,y] > g[x,0:y]).all()) or ((g[x,y] > g[x,y+1:]).all()):
                #print(x,y,g[x,y],((g[x,y] > g[0:x,y]).all()) , ((g[x,y] > g[x:,y]).all()) , ((g[x,y] > g[x,0:y]).all()) , ((g[x,y] > g[x,y:]).all()))
                seen[x,y] = 1
    seen[0,:]=1
    seen[:,0]=1
    seen[:,-1]=1
    seen[-1,:]=1
    #print(seen)
    return seen.sum()

def score(l):
    tally = 0
    for i in l:
        if i>0:
            tally+=1
        else:
            tally+=1
            break
            
    return tally

def part2(g):
    scores = []
    for y in range(1,len(g)-1):
        for x in range(1,len(g[0])-1):
            #distance to tree in each direction
            total_score = 1 
            # same height or edge
            # count the number up to a tree
            left = g[x,y] - g[x,0:y][::-1]
            total_score *= score(left)
            
            right = g[x,y] - g[x,y+1:]
            total_score *= score(right)

            top = g[x,y] - g[0:x,y][::-1]
            total_score *= score(top)

            bot = g[x,y] - g[x+1:,y]
            total_score *= score(bot)
            #if (x,y) == (3,2):
            #    print((x,y),g[x,y],score(top),score(left),score(bot),score(right),g[x,y+1:],right)
            # print(x,y,g[x,y],g[x,0:y][::-1], top, total_score)

            #total = top+bot+left+right
            scores.append(total_score)
    return max(scores)

print(vis(grid))
print(part2(grid))


#assert vis(grid) == 21