def loadlines(daynumber):
    f = open(f'input-{daynumber}.txt','r')
    lines = f.read().split('\n')[:-1]
    f.close()
    return lines