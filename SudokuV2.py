import sys
import time
rawinput = sys.argv[1]
input = rawinput.replace('.', '0')

pzl = []
for i in range(0, len(input)):
    pzl.append(int(input[i]))

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

# lookup = []
# for i in range(0, len(rows)):
#     lookup.append(rows[i])
#     lookup.append(columns[i])
#     lookup.append(boxes[i])
#make lookup set for each box?
#check if sudoku is solved

def pzlInvalid(pzl):
    for i in range(0, len(pzl)):
        if pzl[i] != 0 and pzl[i] in (pzl[j] for j in lookupset[i]):
            return True
    return False

def pzlCompletelySolved(pzl):
    for i in range(0, len(pzl)):
        if (pzl[j] != 0 for j in lookupset[i]) and pzl[i] in (pzl[j] for j in lookupset[i]): ###OMG WHY DOES THIS NOT WORK JESUS CHRIST
            return False
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
for i in range(0, len(emptyinput)-1):
    emptypzl[i] = emptyinput[i]
printSpecial(emptypzl)
print('Solution:')
starttime = time.time()
result = bruteForce(pzl)
endtime = time.time()
if result == '': print('No solution')
else: printSpecial(result)
print('Time:', endtime-starttime)