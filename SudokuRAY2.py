# Sudoku
import time


def generateRows():  # fix
    diction = {}
    for a in range(0, 9):  # 128
        for b in range(0, 9):  # 81
            diction[b + 9 * a] = []  # 128
            for temp in range(0, 9):  # 81
                if (temp != b):
                    diction[b + 9 * a].append(temp + 9 * a)  # 128
    return diction


def generateCols():  # fix
    diction = {}
    for a in range(0, 9):  # 81
        for b in range(0, 9):  # 128
            diction[a + 9 * b] = []  # 81
            for temp in range(0, 9):  # 128
                if (temp != b):
                    diction[a + 9 * b].append(a + 9 * temp)  # 81
    return diction


def generateSquares():
    diction = {}
    for a in range(0, 9):
        for b in range(0, 9):
            diction[b + 9 * a] = []
            startA = int(a / 3) * 1  # *3
            startB = int(b / 3) * 3
            start = startA * 27 + startB
            for temp in range(0, 9):  # shows how the 3x3 square goes
                if (b + 9 * a != start + int(temp / 3) * 9 + temp % 3):  # temp != b
                    addRow = int(temp / 3) * 9
                    addCol = temp % 3
                    diction[b + 9 * a].append(start + addRow + addCol)
    return diction


def isValid(element, spot, L1, L2, L3):
    for num in L1[spot]:
        if (element[spot] == element[num]):
            return False
    for num in L2[spot]:
        if (element[spot] == element[num]):
            return False
    for num in L3[spot]:
        # print('---',spot,num)
        if (element[spot] == element[num]):
            return False
    return True


def bruteForce(state, look1, look2, look3):  # last 3 parameters are look up tables
    if (state[1] == 0):
        return state[0]
    pointList = []
    for i in range(0, len(state[0])):
        if (state[0][i] == "."):
            pointList.append(i)
    possiblesDot = {}
    dotPlace = -1
    size = 10
    allSet = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for empty in pointList:
        seenSet = set()
        prerow = look1[empty]
        precol = look2[empty]
        presqr = look3[empty]
        for i in range(0, 8):
            seenSet.add(state[0][prerow[i]])
            seenSet.add(state[0][precol[i]])
            seenSet.add(state[0][presqr[i]])
        finalSet = allSet - seenSet - {"."}
        possiblesDot[empty] = finalSet
        if (len(finalSet) < size):
            size = len(finalSet)
            dotPlace = empty
    #################################
    element = []
    for thing in state[0]:
        element.append(thing)
    '''
    if(state[1] == 0):
       return element
 
    dotPlace = -1
    for i in range(0, 81):
       if(element[i] == "."):
          dotPlace = i
          break'''
    # print (possiblesDot[dotPlace])
    for num in possiblesDot[dotPlace]:  # 0-9
        newborn = []
        for thing in element:
            newborn.append(thing)
        newborn[dotPlace] = num
        # print (isValid(newborn, dotPlace, look1, look2, look3))
        # if(isValid(newborn, dotPlace, look1, look2, look3)):
        bF = bruteForce((newborn, state[1] - 1), look1, look2, look3)
        if (bF != "none"):
            return bF
    return "none"


startTime = time.clock()
openFile = open("sudokus.txt", "r")
froof = openFile.read()
all = ""
for char in froof:
    if (char != "\n"):
        all += char
looka = generateRows()
lookb = generateCols()
lookc = generateSquares()
# print (lookb[80])




##printspecial
def printSpecial(pzl):
    for i in range(0, 9):
        print(pzl[i*9], pzl[i*9 + 1], pzl[i*9 + 2], '\t',
              pzl[i*9 + 3], pzl[i*9 + 4], pzl[i*9 + 5], '\t',
              pzl[i*9 + 6], pzl[i*9 + 7], pzl[i*9 + 8])
        if (i+1)%3 == 0:
            print()


for a in range(0, 55):  # 13,14 and #16,17 take long time
    puzzle = []
    numDot = 0
    for i in range(0, 81):
        puzzle.append(all[a * 81 + i])
        if (all[a * 81 + i] == "."):
            numDot += 1
    # bF the puzzle for sol
    res = bruteForce((puzzle, numDot), looka, lookb, lookc)
    # output
    print(str(a + 1) + "# puzzle")
    printSpecial(res)
endTime = time.clock()
print("Time taken in seconds: " + str(endTime - startTime))