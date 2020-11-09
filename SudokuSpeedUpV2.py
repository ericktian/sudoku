import time
#1.180739164352417
#184.36805391311646

#lookups
lookupset = [0]*81
for i in range(len(lookupset)):
    lookupset[i] = set()
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

rows2 = [0]*81
for i in range(len(lookupset)):
    lst = rows[int(i//len(lookupset)**.5)]
    rows2[i] = set(lst) - {i}
rows = rows2

cols2 = [0]*81
for i in range(len(lookupset)):
    lst = columns[i%int(len(lookupset)**.5)]
    cols2[i] = set(lst) - {i}
columns = cols2

boxes2 = [0]*81
for i in range(len(lookupset)):
    lst = boxes[3*((i//9)//3) + i%9//3]#boxes[int((len(lookupset)**.5)**.5)*((i//9)//3) + i%(int(len(lookupset)**.5))//3]
    boxes2[i] = set(lst) - {i}
boxes = boxes2

rows2 = [0]*81
for i in range(len(lookupset)):
    # print(int(i//len(lookupset)**.5))
    lst = rows[int(i//len(lookupset)**.5)]
    rows2[i] = set(lst) - {i}
rows = rows2

numberPositions = [0]*10
for i in range(len(numberPositions)):
    numberPositions[i] = set()

def pzlInvalid(pzl, n):
    i = n
    if pzl[i] != 0 and pzl[i] in (pzl[j] for j in lookupset[i]): ### if any set containing i has doubles
        return True
    return False

def pzlCompletelySolved(pzl, n):
    if 0 not in pzl:
        return True
    return False

def bruteForce(pzl, n):
    if pzlInvalid(pzl, n): return ''

    setp = {}
    setp2 = {}
    setinds2 = {}
    if 0 not in pzl: return pzl
    else:
        empty = pzl.index(0)
        setp = set([pzl[i] for i in lookupset[empty]])
        if 0 in setp: setp.remove(0)
        minVal = 9 - len(setp)
        minInd = empty
        for j in range(len(pzl)):
            if pzl[j]==0:
                setofpossiblenumbers = set([pzl[i] for i in lookupset[j]])
                if 0 in setofpossiblenumbers: setofpossiblenumbers.remove(0)
                min = 9 - len(setofpossiblenumbers)
                if min < minVal:
                    setp = setofpossiblenumbers
                    minVal = min
                    minInd = j
        minVal2 = 0  ###
        minInd2 = 0  ###
        group = 0 # 0 = row, 1 = col, 2 = box
        numLeastPos = 0
        for i in range(len(pzl)):
            if pzl[i] == 0:
                for k in range(1, 10):
                    rowset = set(pzl[j] for j in rows[i])
                    colset = set(pzl[j] for j in columns[i])
                    boxset = set(pzl[j] for j in boxes[i])
                    if k not in rowset and len(rowset) > minVal2:
                        minVal2 = len(rowset)
                        minInd2 = i
                        setp2 = rowset
                        setinds2 = set(l for l in rows[i] if pzl[l] == 0 and k not in lookupset[i])
                        group = 0
                        numLeastPos = k
                    if k not in columns and len(colset) > minVal2:
                        minVal2 = len(colset)
                        minInd2 = i
                        setp2 = colset
                        setinds2 = set(l for l in columns[i] if pzl[l] == 0 and k not in lookupset[i])
                        group = 1
                        numLeastPos = k
                    if k not in boxset and len(boxset) > minVal2:
                        minVal2 = len(boxset)
                        minInd2 = i
                        setp2 = boxset
                        setinds2 = set(l for l in boxes[i] if pzl[l] == 0 and k not in lookupset[i])
                        group = 2
                        numLeastPos = k
        # print('minVal', minVal)
        # print('minVal2', minVal2)
        # print('minInd2', minInd2)
        # print('numLeastPos', numLeastPos)
        # printSpecial(pzl)
        # print()
        if minVal <= 9-minVal2:
            emptyIndex = minInd
            posInds = {1, 2, 3, 4, 5, 6, 7, 8, 9} - setp
            for i in posInds:
                subPzl = pzl[:]
                subPzl[emptyIndex] = i
                bF = bruteForce(subPzl, emptyIndex)
                if bF: return bF
        else:
            #print('here')
            emptyIndex = minInd2
            # posInds = {}
            iterate = set()
            if group == 0:
                iterate = rows[emptyIndex]
            if group == 1:
                iterate = columns[emptyIndex]
            if group == 2:
                iterate = boxes[emptyIndex]
            #print(iterate)
            #print(group)

            # iterate2 = set()
            # for i in iterate:
            #     if pzl[i] == 0: iterate2.add(i)
            #print(setinds2)
            #printSpecial(pzl)
            for i in setinds2:
                subPzl = pzl[:]
                subPzl[i] = numLeastPos
                #printSpecial(subPzl)
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

for i in range(13, 14):
    # print(i)
    # print((i.replace('.', '0')))
    list1 = [int(i) for i in list(puzzles[i].replace('.', '0'))]
    # print(list1)
    print(i+1)


    # for i in range(len(list1)):
    #     tempset = set(list1[k] for k in lookupset[i])
    #     for j in range(1, 10):
    #         if j not in tempset:
    #             numberPositions[j].add(i)
    printSpecial(bruteForce(list1, list1.index(0)))
print('Time:', time.time()-starttime)