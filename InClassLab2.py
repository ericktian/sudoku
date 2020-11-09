import sys
pzl = [0]*20
numFaces = int(sys.argv[1])

#lookup
lookup = [[1, 4, 6], [0, 2, 8], [1, 3, 10], [2, 4, 12],
          [0, 3, 14], [6, 14, 15], [0, 5, 7], [6, 8, 16], [1, 7, 9], [8, 10, 17], [2, 9, 11],
          [10, 12, 18], [3, 11, 13], [12, 14, 19], [4, 5, 13],
          [5, 16, 19], [7, 15, 17], [9, 16, 18], [11, 17, 19], [13, 15, 18]]

def pzlInvalid(pzl):
    for i in range(0, len(pzl)):
        for j in lookup[i]:
            if pzl[i] == 1 and pzl[j] == pzl[i]: return True
    return False

def pzlCompletelySolved(pzl):
    #assumes pzlInvalid() has already been called
    if pzl.count(1) == numFaces:
        return True
    return False

def bruteForce(pzl):
    if pzlInvalid(pzl): return ''
    if pzlCompletelySolved(pzl): return pzl

    for i in range(0, len(pzl)):
        if pzl[i] == 0:
            subPzl = pzl[:]
            subPzl[i] = 1
            bF = bruteForce(subPzl)
            if bF: return bF
    return ''

result = bruteForce(pzl)
if result == '': print('No solution')
else:
    print(result)
    ind = []
    for i in range(0, len(result)):
        if result[i]==1:
            ind.append(i)
    print(ind)