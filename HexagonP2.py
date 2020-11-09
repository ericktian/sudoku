import time
start = time.time()
pzl = [0]*24
#lookups
hex1 = [0, 1, 2, 6, 7, 8]
hex2 = [2, 3, 4, 8, 9, 10]
hex3 = [5, 6, 7, 12, 13, 14]
hex4 = [7, 8, 9, 14, 15, 16]
hex5 = [9, 10, 11, 16, 17, 18]
hex6 = [13, 14, 15, 19, 20, 21]
hex7 = [15, 16, 17, 21, 22, 23]
row1 = [0, 1, 2, 3, 4]
row2 = [5, 6, 7, 8, 9, 10, 11]
row3 = [12, 13, 14, 15, 16, 17, 18]
row4 = [19, 20, 21, 22, 23]
row5 = [1, 0, 6, 5, 12]
row6 = [3, 2, 8, 7, 14, 13, 19]
row7 = [4, 10, 9, 16, 15, 21, 20]
row8 = [11, 18, 17, 23, 22]
row9 = [3, 4, 10, 11, 18]
row10 = [1, 2, 8, 9, 16, 17, 23]
row11 = [0, 6, 7, 14, 15, 21, 22]
row12 = [5, 12, 13, 19, 20]
lookup = [hex1, hex2, hex3, hex4, hex5, hex6, hex7,
          row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12]

def pzlInvalid(pzl):
    for i in lookup:
        counts = [0]*8
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k]>1: return True
    return False

def pzlCompletelySolved(pzl):
    if 0 in pzl: return False
    for i in lookup:
        counts = [0]*7
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k] < 1: return False
    return True

def bruteForce(pzl):
    if pzlInvalid(pzl): return ''
    if pzlCompletelySolved(pzl): return pzl

    emptyIndex = pzl.index(0)
    for i in range(1, 8):
        subPzl = pzl[:]
        subPzl[emptyIndex] = i
        bF = bruteForce(subPzl)
        if bF: return bF
    return ''

print(bruteForce(pzl))
print(time.time()-start)