import time
#1.180739164352417
#184.36805391311646

#lookups
lookupset = [{}]*81
rows = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        rows[i].append(i*9+j)
for i in rows:
    for j in i:
        lookupset[j] = set(i)

columns = [[], [], [], [], [], [], [], [], []]
for i in rows:
    for j in range(0, 9):
        columns[j].append(i[j])
for i in columns:
    for j in i:
        lookupset[j].update(set(i))

boxes = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        boxes[i//3 * 3 + j//3].append(rows[i][j])
for i in boxes:
    for j in i:
        lookupset[j].update(set(i))
for i in range(0, len(lookupset)):
    lookupset[i].remove(i)

def pzlInvalid(pzl, n):
    i = n
    if pzl[i] != 0 and pzl[i] in (pzl[j] for j in lookupset[i]):
        return True
    return False

def pzlCompletelySolved(pzl, n):
    if 0 not in pzl:
        return True
    return False

def numPos(n, pzl):
    setp = set([pzl[i] for i in lookupset[n]])
    if 0 in setp: setp.remove(0)
    return 9 - len(setp)

def fewestPos(pzl):
    if 0 not in pzl: return -1
    empty = pzl.index(0)
    minVal = numPos(empty, pzl)
    minInd = empty
    for j in range(len(pzl)):
        if pzl[j]==0:
            min = numPos(j, pzl)
            if min < minVal:
                minVal = min
                minInd = j
    return minInd


def bruteForce(pzl, n):
    if pzlInvalid(pzl, n): return ''

    emptyIndex = fewestPos(pzl)
    if(emptyIndex < 0): return pzl
    for i in range(1, 10):
        subPzl = pzl[:]
        subPzl[emptyIndex] = i
        bF = bruteForce(subPzl, emptyIndex)
        if bF: return bF
    return ''

def printSpecial(pzl):
    for i in range(0, 9):
        print(pzl[i*9], pzl[i*9 + 1], pzl[i*9 + 2], '\t',
              pzl[i*9 + 3], pzl[i*9 + 4], pzl[i*9 + 5], '\t',
              pzl[i*9 + 6], pzl[i*9 + 7], pzl[i*9 + 8])
        if (i+1)%3 == 0:
            print()

file = open("sudokus.txt", "r")
puzzles = file.read().split("\n")
starttime = time.time()
for i in range(0, 128):
    # print(i)
    # print((i.replace('.', '0')))
    list1 = [int(i) for i in list(puzzles[i].replace('.', '0'))]
    # print(list1)
    print(i+1)
    printSpecial(bruteForce(list1, list1.index(0)))
print('Time:', time.time()-starttime)
