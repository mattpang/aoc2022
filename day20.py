from collections import deque
import copy
import utils

lines = utils.loadlines(20)
num = deque([1, 2, -3, 3, -2, 0, 4])
num = deque(list(map(int,lines)))

index = deque(range(0,len(num)))
el = len(num)
s = set()
that = 0
for i in range(len(num)):
    position = index.index(i)
    for deq in [num,index]:
        # print(deq)
        deq.rotate(position*-1)
        this = deq.popleft()
        if deq == num:
            that = this
        deq.rotate(that*-1)
        deq.appendleft(this)

zeroth = num.index(0)
# num.rotate(zeroth*-1)
# print(num)

# print(num[(zeroth+1000)%len(num)])
total = 0
total += num[(zeroth+1000)%len(num)]
total += num[(zeroth+2000)%len(num)]
total += num[(zeroth+3000)%len(num)]
print('part1:',total)

exit()

lines = utils.loadlines(20)

num = deque([x* 811589153 for x in [1, 2, -3, 3, -2, 0, 4]])
num = deque([x* 811589153 for x in list(map(int,lines))])

index = deque(range(0,len(num)))
el = len(num)
that = 0
for j in range(10):
    for i in range(len(num)):
        position = index.index(i)
        for deq in [num,index]:
            deq.rotate(position*-1)
            this = deq.popleft()
            if deq == num:
                that = this
            deq.rotate(that*-1)
            deq.appendleft(this)

zeroth = num.index(0)
total = 0
total += num[(zeroth+1000)%len(num)]
total += num[(zeroth+2000)%len(num)]
total += num[(zeroth+3000)%len(num)]
print('part2:',total)