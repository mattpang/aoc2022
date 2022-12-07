lines = ['$ cd /',
'$ ls',
'dir a',
'14848514 b.txt',
'8504156 c.dat',
'dir d',
'$ cd a',
'$ ls',
'dir e',
'29116 f',
'2557 g',
'62596 h.lst',
'$ cd e',
'$ ls',
'584 i',
'$ cd ..',
'$ cd ..',
'$ cd d',
'$ ls',
'4060174 j',
'8033020 d.log',
'5626152 d.ext',
'7214296 k']

import utils
lines = utils.loadlines(7)

from collections import Counter
c = Counter()
path = []
for line in lines:
    if line.startswith('$ cd'):
        if '..' in line:
            path.pop()
        else:
            path.append(line[len('$ cd '):])
    if line[0].isdigit():
        thispath = []
        for i in range(len(path)):
            thispath.append(path[i])
            c[tuple(thispath)]+=int(line.split(' ')[0])

    #print(path)
#print(c)

# calc total size. 
t = 0
for k,v in c.items():
    if v<=100000 and k!='/':
        t+=v
print(t)
delta = 30000000-(70000000- c[('/',)])
print('reclaim',delta )

values = []
for k,v in c.items():
    if v >= delta:
        values.append(int(v))

print(sorted(values)[0])