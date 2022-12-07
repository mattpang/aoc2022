# want to parse this block, or just hand type it?

#                 [M]     [V]     [L]
# [G]             [V] [C] [G]     [D]
# [J]             [Q] [W] [Z] [C] [J]
# [W]         [W] [G] [V] [D] [G] [C]
# [R]     [G] [N] [B] [D] [C] [M] [W]
# [F] [M] [H] [C] [S] [T] [N] [N] [N]
# [T] [W] [N] [R] [F] [R] [B] [J] [P]
# [Z] [G] [J] [J] [W] [S] [H] [S] [G]
#  1   2   3   4   5   6   7   8   9 

from collections import defaultdict
stack = defaultdict(list)
stack['1'] = ['Z','T','F','R','W','J','G']
stack['2'] = ['G','W','M']
stack['3'] = ['J','N','H','G']
stack['4'] = ['J','R','C','N','W']
stack['5'] = ['W','F','S','B','G','Q','V','M']
stack['6'] = ['S','R','T','D','V','W','C']
stack['7'] = ['H','B','N','C','D','Z','G','V']
stack['8'] = ['S','J','N','M','G','C']
stack['9'] = ['G','P','N','W','C','J','D','L']


# stack = defaultdict(list)
# stack['1'] = ['Z','N']
# stack['2'] = ['M','C','D']
# stack['3'] = ['P']

# lines = ['move 1 from 2 to 1',
# 'move 3 from 1 to 3',
# 'move 2 from 2 to 1',
# 'move 1 from 1 to 2']

import utils
def part1(stack,lines):
    #lines = utils.loadlines(5)
    # part 1
    for line in lines:
        if line.startswith('move'):
            #line.split()
            print(line)
            c = line.split(' ')
            print(c)
            amt = int(c[1])
            src = c[3]
            dest = c[5]
            print(amt,src,dest)
            taken = []
            for m in range(amt):
                print(m)
                taken.append(stack[src].pop())
            print(taken)
            stack[dest] += taken
        print(stack)
    ans = []
    for i in sorted(stack.keys()):
        ans.append(stack[str(i)][-1])

    print(''.join(ans))

# part 2, the pop is different now. we take the list as was.

def part2(stack,lines):
    # part 1
    for line in lines:
        if line.startswith('move'):
            #line.split()
            print(line)
            c = line.split(' ')
            print(c)
            amt = int(c[1])
            src = c[3]
            dest = c[5]
            print(amt,src,dest)
            taken = []
            for m in range(amt):
                print(m)
                taken.append(stack[src].pop())
            print(taken)
            stack[dest] += taken[::-1]
        print(stack)
    ans = []
    for i in sorted(stack.keys()):
        ans.append(stack[str(i)][-1])

    print(''.join(ans))

lines = utils.loadlines(5)
part2(stack=stack,lines=lines)