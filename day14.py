lines = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.split('\n')
import utils
lines = utils.loadlines(14)
import copy

from collections import Counter
grid = Counter()
ally=[]
allx=[]
for line in lines:
    el = line.split(' -> ')
    for e in el:
        for x1,x2 in zip(el[:-1],el[1:]):
            a = tuple(map(int,x1.split(',')))
            b = tuple(map(int,x2.split(',')))
            #print(a,b)
            if abs(a[0]-b[0]) >0:
                smallx = min(a[0],b[0])
                largex = max(a[0],b[0])
                for x in range(smallx,largex+1):
                    grid[(x,a[1])]=2

            if abs(a[1]-b[1]) >0:
                smally = min(a[1],b[1])
                largey = max(a[1],b[1])

                for y in range(smally,largey+1):
                    grid[(a[0],y)]=2
            
            #everything from x,y to x1,y1 is 2
            #grid[xy] = 2
            ally.append(a[1])
            ally.append(b[1])
            allx.append(a[0])
            allx.append(b[0])

maxy = max(ally)

# add an inf line of sand at maxy+2

#print(grid)
for y in range(maxy+1):
    line = ''
    for x in range(min(allx),max(allx)+1):
        #print(x,y,grid[(x,y)])
        if grid[(x,y)]==2:
            line+='#'
        elif grid[(x,y)]==1:
            line+='o'
        else:
            line+='.'
    #ans.append(line)
    print(line)

print('')
print('')

def sim(grid,part2=False):
    sandpoint = (500,0)
    #print(grid)
    grains = 0
    current = list(sandpoint)
    tally = 1
    while True:
        #print(current)
        if current[1]==maxy+1 and part2:
            # hit the floor, trigger
            grid[(current[0],current[1])] = 1
            current = list(sandpoint)
            #print('rest')
            grains+=1

        if grid[(current[0],current[1]+1)]==0:
            current = [current[0],current[1]+1]
            #print('drop')
        elif grid[(current[0],current[1]+1)]>0:
            if grid[(current[0]-1,current[1]+1)]==0:
                # go left
                current = [current[0]-1,current[1]+1]
                #print('left')
            elif grid[(current[0]+1,current[1]+1)]==0:
                current = [current[0]+1,current[1]+1]
                #print('right')
            else:
                # at rest
                grid[(current[0],current[1])] = 1
                current = list(sandpoint)
                #print('rest')
                grains+=1

        if current[1]>=maxy and not part2:
            grid[(current[0],current[1])] = 5
            print('this overfilled at:',current)
            break

        if grid[sandpoint]>0 and part2:
            break
        # if tally > 2000:
        #     break
        # tally+=1
    print(grains)

clean_grid = copy.deepcopy(grid)
sim(grid,part2=False)
sim(clean_grid,part2=True)
exit()

ans = []

#print(grid)
for y in range(0,maxy+2):
    line = str(y).zfill(4)+'|'
    for x in range(min(allx)-1,max(allx)+1):
        #print(x,y,grid[(x,y)])
        if x==500 and y==0:
            line+='+'
        if grid[(x,y)]==2:
            line+='#'
        elif grid[(x,y)]==1:
            line+='o'
        elif grid[(x,y)]==5:
            line+='~'
        else:
            line+='.'
    #ans.append(line)
    print(line)
print(grains)
print('this overfilled at:',current)
