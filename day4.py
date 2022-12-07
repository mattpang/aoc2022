import utils
lines = utils.loadlines(4)

# lines = ['2-4,6-8',
# '2-3,4-5',
# '5-7,7-9',
# '2-8,3-7',
# '6-6,4-6',
# '2-6,4-8']

tally = 0
for line in lines:
    l1,l2 = line.replace('\n','').split(',')
    # print(l1,l2)
    l1_1, l1_2 = map(int,l1.split('-'))
    l2_1, l2_2 = map(int,l2.split('-'))

    if (int(l1_1)<=int(l2_1) and int(l1_2)>=int(l2_2)) or (int(l1_1)>=int(l2_1) and int(l1_2)<=int(l2_2)):
        tally+=1
print(tally)


# overlaps at all.
tally = 0
for line in lines:
    l1,l2 = line.replace('\n','').split(',')
    # print(l1,l2)
    l1_1, l1_2 = map(int,l1.split('-'))
    l2_1, l2_2 = map(int,l2.split('-'))
    overlap = len(list(set(range(l1_1,l1_2+1)).intersection(set(range(l2_1,l2_2+1)))))
    if overlap>0:
        tally+=1
print(tally)