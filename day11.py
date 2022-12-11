import utils
from collections import defaultdict, Counter
import numpy as np


lines = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''.split('\n')
lines = utils.loadlines(11)

#a = np.genfromtxt('input-8.txt',delimiter=1,dtype=int)
#print(a)
global m
m = dict()

class monkey():
    
    def __init__(self) -> None:
        self.worry = 1
        self.inspected = 0 
        pass
    def printstats(self):
        print(self.id, self.start, self.intruct, self.mod, self.tcase,self.fcase)
    
    def calc(self,part1=True):
        for s in range(len(self.start)):
            self.worry *= self.start.pop(0)
            self.inspected+=1
            old = self.worry
            # print('starting:',self.worry)
            # print(self.intruct)
            self.worry = eval(self.intruct)
            # print(self.worry)
            # print(self.worry,self.mod)
            if part1:
                print('div 3')
                self.worry=self.worry//3
            else:
                self.worry %= self.lcm

            if self.worry%self.mod==0:
                m[self.tcase].start.append(self.worry)
                # print(f'true, go to {self.tcase} with {self.worry}')
            else:
                m[self.fcase].start.append(self.worry)
                # print(f'false, go to {self.fcase} with {self.worry}')
            self.worry=1
            # print('')


total = 0 
mcount=0
for line in lines: 
    line.split(' ')
    if line.startswith('Monkey'):
        m[mcount] = monkey()
        m[mcount].id = mcount
        mcount+=1
    elif line.startswith('  Starting items'):
        m[mcount-1].start = list(map(int,line.split(':')[-1].strip().split(', ')))
    elif line.startswith('  Operation:'):
        m[mcount-1].intruct = line.split('=')[-1].strip()
    elif line.startswith('  Test:'):
        m[mcount-1].mod = int(line.split(' ')[-1])
    elif 'true' in line:
        m[mcount-1].tcase = int(line.split(' ')[-1])
    elif 'false' in line:
        m[mcount-1].fcase = int(line.split(' ')[-1])
    else:
        pass

print(m)

for i in range(mcount):
    m[i].printstats()

lcm = 1
divs = []
for i in range(len(m)):
    divs.append(m[i].mod)
for x in divs:
    lcm *= (lcm*x)
for i in range(len(m)):
    m[i].lcm = lcm

for r in range(20):
    #print('r:',r)
    # if r%100==0:
    #     print(r)
    #     for i in range(len(m)):
    #         print(i,m[i].inspected)

    for i in range(len(m)):
        m[i].calc(part1=False)
topm = []
for i in range(len(m)):
    # print(m[i].inspected)
    topm.append(m[i].inspected)
t = sorted(topm)[::-1]
print('part1:')
print(t[0]*t[1])
print('part2:')

for r in range(10000):
    #print('r:',r)
    # if r%100==0:
    #     print(r)
    #     for i in range(len(m)):
    #         print(i,m[i].inspected)

    for i in range(len(m)):
        m[i].calc(part1=False)

topm = []
for i in range(len(m)):
    # print(m[i].inspected)
    topm.append(m[i].inspected)
t = sorted(topm)[::-1]
print(t[0]*t[1])