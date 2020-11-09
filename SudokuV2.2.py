import sys
import time
rawinput = sys.argv[1]
input = rawinput.replace('.', '0')

pzl = []
for i in range(0, len(input)):
    pzl.append(int(input[i]))

#lookups
lookupdict = {}
rows = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        rows[i].append(i*9+j)
for i in rows:
    for j in i:
        lookupdict[j] = set(i)

columns = [[], [], [], [], [], [], [], [], []]
for i in rows:
    for j in range(0, 9):
        columns[j].append(i[j])
for i in columns:
    for j in i:
        lookupdict[j].update(set(i))

boxes = [[], [], [], [], [], [], [], [], []]
for i in range(0, 9):
    for j in range(0, 9):
        boxes[i//3 * 3 + j//3].append(rows[i][j])
for i in boxes:
    for j in i:
        lookupdict[j].update(set(i))
for i in range(0, len(lookupdict)):
    lookupdict[i].remove(i)

# lookup = []
# for i in range(0, len(rows)):
#     lookup.append(rows[i])
#     lookup.append(columns[i])
#     lookup.append(boxes[i])
#make lookup set for each box?
#check if sudoku is solved

def pzlInvalid(pzl, n):
    i = n
    if pzl[i] != 0 and pzl[i] in (pzl[j] for j in lookupdict[i]):
        return True
    return False

def pzlCompletelySolved(pzl, n):
    # i = n
    # if pzl[i] in (pzl[j] for j in lookupset[i]) or (pzl[j]==0 for j in lookupset[i]):
    #     return False
    # return True
    if 0 not in pzl:
        return True
    return False


def bruteForce(pzl, n):
    if pzlInvalid(pzl, n): return ''
    if pzlCompletelySolved(pzl, n): return pzl

    # printSpecial(pzl)
    emptyIndex = pzl.index(0)
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

print('\nPuzzle:')
emptyinput = rawinput.replace('.', '_')
emptypzl = ['']*81
for i in range(0, len(emptyinput)-1):
    emptypzl[i] = emptyinput[i]
printSpecial(emptypzl)
print('Solution:')
starttime = time.time()
# print(pzl)
result = bruteForce(pzl, pzl.index(0))
endtime = time.time()
if result == '': print('No solution')
else: printSpecial(result)
print('Time:', endtime-starttime)