f = open('input-3.txt','r')
lines = f.read().split('\n')[:-1]
f.close()

#lines = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']
total = 0
for line in lines:
    a = set([x  for x in line[0:len(line)//2]])
    b = set([x for x in line[len(line)//2:]])
    common = list(a.intersection(b))[0]
    if common.isupper():
        score = ord(common)-65+27
    else:
        score = ord(common)-96
    total+=score 
print(total)

#lines = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']
# part 2, for every 3 lines, what's the intersection.
total = 0
for i in range(len(lines)//3):
    #print(lines[i*3],lines[i*3+1],lines[i*3+2])
    common = list((set(lines[i*3]).intersection(set(lines[i*3+1])).intersection(set(lines[i*3+2]))))[0]
    if common.isupper():
        score = ord(common)-65+27
    else:
        score = ord(common)-96
    total+=score 
print(total)