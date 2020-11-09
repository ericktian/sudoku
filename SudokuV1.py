import sys
import time
rawinput = sys.argv[1]
input = rawinput.replace('.', '0')

pzl = []
for i in range(0, len(input)):
    pzl.append(int(input[i]))

#lookups
rows = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        rows[i].append(i*9+j)
columns = [[], [], [], [], [], [], [], [], []]
for i in rows:
    for j in range(0, 9):
        columns[j].append(i[j])
boxes = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        boxes[i//3 * 3 + j//3].append(rows[i][j])
lookup = []
for i in range(0, len(rows)):
    lookup.append(rows[i])
    lookup.append(columns[i])
    lookup.append(boxes[i])

def pzlInvalid(pzl):
    for i in lookup:
        counts = [0]*10
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k]>1: return True
    return False

def pzlCompletelySolved(pzl):
    for i in lookup:
        counts = [0]*10
        for j in i:
            counts[pzl[j]] += 1
        for k in range(1, len(counts)):
            if counts[k] != 1: return False
    return True

def bruteForce(pzl):
    if pzlInvalid(pzl): return ''
    if pzlCompletelySolved(pzl): return pzl

    emptyIndex = pzl.index(0)
    for i in range(1, 10):
        subPzl = pzl[:]
        subPzl[emptyIndex] = i
        bF = bruteForce(subPzl)
        if bF: return bF
    return ''

def printSpecial(pzl):
    for i in range(0, 9):
        print(pzl[i*9], pzl[i*9 + 1], pzl[i*9 + 2], '\t',
              pzl[i*9 + 3], pzl[i*9 + 4], pzl[i*9 + 5], '\t',
              pzl[i*9 + 6], pzl[i*9 + 7], pzl[i*9 + 8])
        if (i+1)%3 == 0:
            print()

print('\nPuzzle:')
emptyinput = rawinput.replace('.', '_')
emptypzl = ['']*81
for i in range(0, len(emptyinput)):
    emptypzl[i] = emptyinput[i]
printSpecial(emptypzl)
print('Solution:')
starttime = time.time()
result = bruteForce(pzl)
endtime = time.time()
if result == '': print('No solution')
else: printSpecial(result)
print('Time:', endtime-starttime)