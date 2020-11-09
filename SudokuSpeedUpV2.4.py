import time
#SAME AS 2.3

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


NEWlookupset = [set() for _ in range(81)] #make list of sets that contain the index
for i in range(len(NEWlookupset)):
    for j in rows:
        if i in j:
            NEWlookupset[i].update(set(j))
    for k in columns:
        if i in k:
            NEWlookupset[i].update(set(k))
    for l in boxes:
        if i in l:
            NEWlookupset[i].update(set(l))

def pzlInvalid(pzl, n):
    if pzl[n] in (set().union(i) for i in NEWlookupset[n]):
        return True
    return False

def pzlCompletelySolved(pzl, n):
    if 0 not in pzl:
        return True
    return False


def bruteForce(pzl, n):
    if 0 not in pzl: return pzl

    ### Speed up 1
    fastest = False
    empty = pzl.index(0)
    setp = set([pzl[i] for i in lookupset[empty]]) - {0}
    minVal = 9 - len(setp)
    minInd = empty
    for j in range(len(pzl)):
        if pzl[j]==0:
            setofpossiblenumbers = set([pzl[i] for i in lookupset[j]]) - {0}
            min = 9 - len(setofpossiblenumbers)
            if min < minVal:
                setp = setofpossiblenumbers
                minVal = min
                minInd = j
                if min == 1:
                    fastest = True
                    break

    ### Speed up 2
    if not fastest:
        setp2 = set()
        minVal2 = 10
        minNum2 = 0
        possibilities = [set() for i in range(81)]
        for i in range(len(pzl)):
            if pzl[i] == 0:
                tempset = set()
                for j in lookupset[i]:
                    tempset.add(pzl[j])
                for k in range(1, 10):
                    if k not in tempset:
                        possibilities[i].add(k)


        row_numToInds = [[set() for i in range(9)] for j in range(10)]  # list where index = #, index of list in that index = row #
        col_numToInds = [[set() for i in range(9)] for j in range(10)]  # NOTE: row_numToInds[0] is just set()
        box_numToInds = [[set() for i in range(9)] for j in range(10)]
        for i in range(1, 10):
            if minVal2 == 1:
                break
            for j in range(9):
                for k in range(9):
                    if 0 == pzl[rows[j][k]] and i in possibilities[rows[j][k]]:
                        row_numToInds[i][j].add(rows[j][k])
                if len(row_numToInds[i][j]) > 0 and len(row_numToInds[i][j]) < minVal2:
                    minVal2 = len(row_numToInds[i][j])
                    minNum2 = i
                    setp2 = row_numToInds[i][j]
                    if minVal2 == 1:            ###added this later, improved from 37 to 35
                        break
                for k in range(9):
                    if 0 == pzl[columns[j][k]] and i in possibilities[columns[j][k]]:
                        col_numToInds[i][j].add(columns[j][k])
                if len(col_numToInds[i][j]) > 0 and len(col_numToInds[i][j]) < minVal2:
                    minVal2 = len(col_numToInds[i][j])
                    minNum2 = i
                    setp2 = col_numToInds[i][j]
                    if minVal2 == 1:
                        break
                for k in range(9):
                    if 0 == pzl[boxes[j][k]] and i in possibilities[boxes[j][k]]:
                        box_numToInds[i][j].add(boxes[j][k])
                if len(box_numToInds[i][j]) > 0 and len(box_numToInds[i][j]) < minVal2:
                    minVal2 = len(box_numToInds[i][j])
                    minNum2 = i
                    setp2 = box_numToInds[i][j]
                    if minVal2 == 1:
                        break
    else:
        minVal2 = 2

    if minVal <= minVal2:
        emptyIndex = minInd
        posInds = {1, 2, 3, 4, 5, 6, 7, 8, 9} - setp
        for i in posInds:
            subPzl = pzl[:]
            subPzl[emptyIndex] = i
            bF = bruteForce(subPzl, emptyIndex)
            if bF: return bF
        return ''
    else:
        for i in setp2:
            subPzl2 = pzl[:]
            subPzl2[i] = minNum2
            bF = bruteForce(subPzl2, i)
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
    list1 = [int(i) for i in list(puzzles[i].replace('.', '0'))]
    print(i+1)
    printSpecial(bruteForce(list1, list1.index(0)))
print('Time:', time.time()-starttime)