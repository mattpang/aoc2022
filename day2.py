f = open('input-2.txt','r')
lines = f.read().split('\n')[:-1]
f.close()

# lines = ['A Y',
# 'B X',
# 'C Z']
from collections import deque

def run(combo):
    lookup = {'A':'R','B':'P','C':'S'}
    lookup.update(combo)
    print(lookup)
    rules = {'RP':6,'PS':6,'SR':6,'SP':0,'PR':0,'RS':0,'RR':3,'SS':3,'PP':3}
    worth = {'R':1,'P':2,'S':3}
    round_score = 0
    for line in lines:
        #print(line)
        #print(line[0],line[2])
        items = line.replace('/n','').split(' ')

        them = items[0]
        me = items[1]
        round_score += rules[lookup[them]+lookup[me]] + worth[lookup[me]]

    return round_score

#combo = {'X':'R','Y':'P','Z':'S'}
c = deque(['R','P','S'])
for i in range(3):
    c.rotate(1)
    combo = {'X':c[0],'Y':c[1],'Z':c[2]}
    print(combo)
    print(run(combo))


def run_part2():
    lookup = {'A':'R','B':'P','C':'S'}
    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
    myrule = {('R','X'):3+0,('R','Y'):+1+3,('R','Z'):2+6,
            ('P','X'):1+0,('P','Y'):+2+3,('P','Z'):3+6,
            ('S','X'):2+0,('S','Y'):+3+3,('S','Z'):1+6,}
    round_score = 0
    for line in lines:
        items = line.replace('/n','').split(' ')

        them = items[0]
        me = items[1]
        lookup[them]
        round_score += myrule[(lookup[them],me)]

    return round_score

print(run_part2())