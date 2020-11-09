import sys
pzl = [0]*20
numColors = int(sys.argv[1])

#lookup
lookup = [[1, 4, 6], [0, 2, 8], [1, 3, 10], [2, 4, 12],
          [0, 3, 14], [6, 14, 15], [0, 5, 7], [6, 8, 16], [1, 7, 9], [8, 10, 17], [2, 9, 11],
          [10, 12, 18], [3, 11, 13], [12, 14, 19], [4, 5, 13],
          [5, 16, 19], [7, 15, 17], [9, 16, 18], [11, 17, 19], [13, 15, 18]]

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
else:
    print(result)
    output = result[:]
    for i in range(0, len(output)):
        if output[i] == 1: output[i] = 'A'
        if output[i] == 2: output[i] = 'B'
        if output[i] == 3: output[i] = 'C'
        if output[i] == 4: output[i] = 'D'
    print(''.join(output))