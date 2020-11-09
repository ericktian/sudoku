import sys
pzl = [0]*12
numFaces = int(sys.argv[1])

#lookup
lookup = [[1, 2, 3, 4, 5], [0, 2, 5, 6, 7], [0, 1, 3, 7, 8], [0, 2, 4, 8, 9], [0, 3, 5, 9, 10], [0, 1, 4, 6, 10],
          [1, 5, 7, 10, 11], [1, 2, 6, 8, 11], [2, 3, 7, 9, 11], [3, 4, 8, 10, 11], [4, 5, 6, 9, 11], [6, 7, 8, 9, 10]]

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
else: print(result)