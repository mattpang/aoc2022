f = open('input-1.txt','r')
lines = f.read().split('\n')[:-1]
f.close()
each_cal = []
cal = 0
for line in lines:

    if len(line) == 0:
        each_cal.append(cal)
        cal = 0
        
    else:
        cal+=int(line)
print(max(each_cal))
s = sorted(each_cal)[::-1]
print(s[0]+s[1]+s[2])
