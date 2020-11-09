import sys
pzl = [0]*12
numColors = int(sys.argv[1])

#lookup
lookup = [[1, 2, 3, 4, 5], [0, 2, 5, 6, 10], [0, 1, 3, 6, 7], [0, 2, 4, 7, 8], [0, 3, 5, 8, 9], [0, 1, 4, 9, 10],
          [1, 2, 7, 10, 11], [2, 3, 6, 8, 11], [3, 4, 7, 9, 11], [4, 5, 8, 10, 11], [1, 5, 6, 9, 11], [6, 7, 8, 9, 10]]

def pzlInvalid(pzl):
    for i in range(0, len(pzl)):
        for j in lookup[i]:
            if pzl[i] != 0 and pzl[j] == pzl[i]: return True
    return False

def pzlCompletelySolved(pzl):
    #assumes pzlInvalid() has already been called
    if 0 not in pzl and len(set(pzl)) <= numColors:
        return True
    return False

def bruteForce(pzl):
    if pzlInvalid(pzl): return ''
    if pzlCompletelySolved(pzl): return pzl

    emptyIndex = pzl.index(0)
    for i in range(1, numColors + 1):
        subPzl = pzl[:]
        subPzl[emptyIndex] = i
        bF = bruteForce(subPzl)
        if bF: return bF
    return ''

result = bruteForce(pzl)
if result == '': print('No solution')
else: print(result)