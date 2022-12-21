lines = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''.split('\n')
import utils
lines = utils.loadlines(21)
import copy
val = dict()
todo = set()
for line in lines:
    p1,p2 = line.split(': ')
    if p2.isdigit():
        val[p1] = int(p2)
    else:
        a = tuple(p2.split(' '))
        print(p2)
        todo.add(a)
        val[p1] = a

def part1(val):
    while True:
        if type(val['root'])==int:
            break
        for k,v in val.items():
            if type(v) == tuple:
                #print(k,v)
                if type(val[v[0]])==int and type(val[v[2]]) == int:
                    #print(k)
                    #break
                    if v[1] == '/':
                        val[k] = eval(str(val[v[0]])+v[1]+v[1]+str(val[v[2]]))
                    else:
                        val[k] = eval(str(val[v[0]])+v[1]+str(val[v[2]]))
                    
                    #print(k,val[k])
    print(val['root'])


from numpy.polynomial import Polynomial

def part2(guess,val):
    # expand the equation for root. 
    # then we replace
    val['humn'] = Polynomial([0, 1])
    val['root'] = (val['root'][0],'-',val['root'][2])
    while True:
        if type(val['root'])==int or isinstance(val['root'], Polynomial):
            return val['root']
            break
        for k,v in val.items():
            if type(v) == tuple:
                #print(k,v)
                if isinstance(val[v[0]], (int, Polynomial)) and isinstance(val[v[2]], (int, Polynomial)):
                    #print(k)
                    #break
                    if v[1] == '/':
                        val[k] = val[v[0]]//val[v[2]]
                    if v[1] == '+':
                        val[k] = val[v[0]]+val[v[2]]
                    if v[1] == '-':     
                        val[k] = val[v[0]]-val[v[2]]                    
                    if v[1] == '*':     
                        val[k] = val[v[0]]*val[v[2]]
#        print(val['root'])


    # left = val['root'][0]
    # right = val['root'][1]

    # # trace all the bits of left and right. Leave in terms of x.
    # for k,v in val.items():
        


# part1(copy.deepcopy(val))
# print('')
result = part2(0,copy.deepcopy(val))
print(result)
print(round(result.roots()[0]))


# 0 and 1 gives 110294985052700


# can't do it with brute force. 
# while True:
#     b = part2(bot,copy.deepcopy(val))
#     t = part2(top,copy.deepcopy(val))
#     print(top,bot,b,t)
#     if b>=0:
#         bot += -100
#     if b<0:
#         bot += 100
#     if t>=0:
#         top -= 100
#     if t<0:
#         top += 100
#     elif b==t:
#         break

# print(part2(bot,copy.deepcopy(val)))