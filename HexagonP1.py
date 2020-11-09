pzl = [0]*24
#lookups
hex1 = [0, 1, 2, 6, 7, 8]
hex2 = [2, 3, 4, 8, 9, 10]
hex3 = [5, 6, 7, 12, 13, 14]
hex4 = [7, 8, 9, 14, 15, 16]
hex5 = [9, 10, 11, 16, 17, 18]
hex6 = [13, 14, 15, 19, 20, 21]
hex7 = [15, 16, 17, 21, 22, 23]
lookup = [hex1, hex2, hex3, hex4, hex5, hex6, hex7]

def pzlInvalid(pzl):
    for i in lookup:
        counts = [0]*7
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k]>1: return True
    return False

def pzlCompletelySolved(pzl):
    for i in lookup:
        counts = [0]*7
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k] != 1: return False
    return True

def bruteForce(pzl):
    if pzlInvalid(pzl): return ''
    if pzlCompletelySolved(pzl): return pzl

    emptyIndex = pzl.index(0)
    for i in range(1, 7):
        subPzl = pzl[:]
        subPzl[emptyIndex] = i
        bF = bruteForce(subPzl)
        if bF: return bF
    return ''

result = bruteForce(pzl)
if result == '': print('No solution')
else: print(result)