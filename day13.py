lines = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''.split('\n\n')

def checklist(a,b):
    if len(a)>len(b):
        return 1
    elif type(a[0]) == list and type(b[0])== list:
        for i in range(len(a)):
            checklist(a[i],b[i])
    else:
        return 0


def compare(l,r):

    lsize = len(l)
    rsize = len(r)

    maxn = max(lsize,rsize)

    for i in range(maxn):
        if i >= lsize: 
            return 1
        if i>= rsize:
            return 0

        a = l[i]
        b = r[i]

        if (type(a) == int) and (type(b)== int):
            if a<b:
                return 1
            elif a>b:
                return 0
        else:
            if type(a) == int:
                a=[a]
            if type(b) == int:
                b=[b]
            ans = compare(a,b)
            if ans is not None:
                return ans

f = open('input-13.txt','r')
lines = f.read().split('\n\n')
f.close()
print(len(lines))

score = 0
for i,line in enumerate(lines):
    a,b = line.split('\n')
    l = eval(a)
    r = eval(b)

    c = compare(l,r)
    #if type(c) == int:
    if c == 1:
        score+=i+1

print(score)

f = open('input-13.txt','r')
lines = list(map(eval,f.read().replace('\n\n','\n').split('\n'))) +[[[2]]]+[[[6]]]
f.close()

def sorter(lines):
    for i in range(len(lines)-1):
        for j in range(len(lines)-i-1):
            if compare(lines[j+1],lines[j]):
                lines[j] , lines[j+1] = lines[j+1] , lines[j]

sorter(lines)
for i, v in enumerate(lines,1):
    if v == [[2]]:
        ans=i
    if v == [[6]]:
        ans*=i
print(ans)