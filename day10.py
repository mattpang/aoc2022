from collections import defaultdict
import utils
lines = utils.loadlines(10)

val = 1
cycle_count = 1
tmp = 0 
total = 0 
outs = (20,60,100,140,180,220)
print(cycle_count,val)
c = 0 
cycle_values = defaultdict(int)
cycle_added = dict()
cycle_added[1] = 1

# I don't think i should loop the lines. 
for i,line in enumerate(lines):
    val+=val
    if line.startswith("noop"):
        cycle_count+=1
        pass
    elif line.startswith('addx'):
        tmp = int(line.split(' ')[1])
        cycle_count+=2
        cycle_added[cycle_count] = tmp

total = 0 
subtotal = 0
for i in range(1,221):
    try:
        subtotal+=cycle_added[i]
    except KeyError:
        pass
    if i in outs:
        total += subtotal*outs[c]
        c+=1

print(total)

# drawing pixels
# if one of the 3 pixels overlaps with current pos, it is a true
subtotal = 0
store = []
for i in range(6):
    l = ''
    for x in range(1+i*40,(i+1)*40+1):
        try:
            subtotal+=cycle_added[x]
        except KeyError:
            pass
        #print(x,subtotal)
        if subtotal-1 <= x-(i*40)-1 <= subtotal+1 :
            l+='#'
        else:
            l+='.'
    print(l)