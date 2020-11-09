import time
starttime = time.time()

f = open("sudokus.txt", "r")
edges = f.read().split()
sets = {}
index = 1
for i in range(0,9):
    subS = set([])
    for j in range(1,10):
        subS.add(9*i + j)
    sets[index] = subS
    index+=1
for i in range(1,10):
    subS = set([])
    for j in range(0,9):
        subS.add(i + j*9)
    sets[index] = subS
    index+=1
base = [1,2,3,10,11,12,19,20,21]
for i in range (0,3):
    for j in range(0,3):
        numToAdd = 27*i + 3*j
        subS = [(numToAdd + base[k]) for k in range(0,9)]
        sets[index] = set(subS)
        index += 1
posToSets, posToNei = {}, {}
for i in range(1, 82):
    posToSets[i] = []
for k, v in sets.items():
    for e in v:
        posToSets[e].append(k)
for i in posToSets:
     poss = []
     for s in posToSets[i]:
         poss += sets[s]
     posToNei[i] = set(poss)
     posToNei[i] -= {i}
def isInvalid(pzl, uP):
    for i in posToSets[uP]:
        if (hasDup(sets[i], pzl)): return 1
    return 0
def hasDup(s, pzl):
    count = [0]*10
    vals = [pzl[j] for j in s]
    for k in vals:
        if (k != 0):
            count[k] +=1
            if count[k] > 1:
                return 1
def isSolved(pzl):
    return not 0 in pzl[1:]
def bruteForce(pzl, uP):
    if isInvalid(pzl, uP): return ""
    if isSolved(pzl): return pzl
    # uP = 1
    arr = [0]*82
    for u in range(1,82):
        p = [pzl[i] for i in posToNei[u]] + [pzl[u]]
        setp = set(p)
        setp.discard(0)
        # print("Vals at: ", u , setp)
        arr[u] = 9-len(setp)
        if pzl[u] != 0:
            arr[u] = 0
    uP = pzl[1:].index(0)+1#next((index for index,value in enumerate(arr) if value != 0), None)
    #print(arr)
    for i in range(1,82):
        if arr[i] !=0 and arr[i] < arr[uP] and pzl[i] == 0:
            uP = i
    # while uP < 82:
    #     if pzl[uP] != 0:
    #         uP +=1
    #     else:
    #         break
    x = set([pzl[i] for i in posToNei[uP]])
    x = {1,2,3,4,5,6,7,8,9} - x
    for j in x:
        subPzl = pzl[:]
        subPzl[uP] = j
        bF = bruteForce(subPzl, uP)
        if bF: return bF
    return ""
def printPzl(s):
    for i in range(0,81):
        if i%27==0:
            print()
        if i%9 == 0:
            print()
        elif i%3 == 0:
            print("  ", end='')
        if s[i] == 0: print("-", " ", end='')
        else: print(str(s[i]), " ", end='')
    print()
    print()
def transform(i):
    boxes = edges[i][:]
    boxes = list(boxes)
    boxes = ["."] + boxes
    boxes = [0 if x == "." else int(x) for x in boxes]
    return boxes

for a in range(0, 128):
    boxes = transform(a)
    print("ORIGINAL ", "(", a+1, "):", end='')
    printPzl(boxes[1:])
    t = bruteForce(boxes, 1)
    if t:
        print("SOLUTION ", "(", a+1, "):", end='')
        printPzl(t[1:])
    else: print("NO SOLUTION")
print("TIME TAKEN: ", time.time()-starttime)