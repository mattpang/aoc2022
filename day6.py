
def packet(s,marker=4):
    # if the last 4 digits are all unique, return position

    for i in range(marker,len(s)):
        if len(set(s[i-marker:i])) == marker:
            #print(i,s[i-4:i])
            return i

assert packet('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert packet('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert packet('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert packet('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

import utils
lines = utils.loadlines(6)
total = 0

print(packet(lines[0],marker=4))
assert packet('mjqjpqmgbljsphdztnvjfqwrcgsmlb',marker=14) == 19

print(packet(lines[0],marker=14))
