# #A
#easy
# #B
# pzl = '814976532.5.123478.3.854169948265317275341896163798245391682754587439621426517983'
# B = {i for i in range(len(pzl)) if pzl[i]=='.'}
# print(B)
# #C
# C = [set() for i in range(40)]
# print(C)
# print(len(C))
# #D
# lstStr = ['', '2', '3', '', '', '4', '']
# D = sum(i=='' for i in lstStr)
# print(D)
###################### #E
# E = {k for k in [{*range(i, i+4)} for i in range(12, 93, 10)]}

# E = {i for i in range(9, 96) if i%10>1 and i%10<6}
#
# print(E)
# #F
# #hopefully this is right
# #G
# myDct = {'foo':23, 'bar':45, 'baz':31}
# G = {myDct[i]:i for i in myDct}
# print(G)
# #H
# myStr = 'abcdefgh'
# H = myStr[0::2]
# print(H)
# #I
# mySet = {2, 4, 5, 6, 7, 8}
# I = min(mySet-{min(mySet)})
# print(I)
# #J
# lstOfLstsOfInts = [[0, 2, 3], [4, 2, 5], [5, 6, 7]]
# J = [[*i] for i in lstOfLstsOfInts]
# print(J)
# #K
# K = [chr(i+97)+str(j+1) for j in range(9) for i in range(9)]
# print(K)
# #L
# lstInts = [1, 3, 2, 5, 4, -1, 0]
# L = sum(lstInts[i]>lstInts[i+1] for i in range(len(lstInts)-1))
# print(L)
# #M
# M = [i for i in range(99) if i%3*i%7]
# print(M)
# #N
# N = {i for i in range(99) if not (i%3 or i%7)}
# print(N)
# # #O
dct = {'bar':45, 'foo':23, 'baz':31}
# O = {dct[i]:i for i in dct}[(min(dct.values()))]
O = dct.get(min(dct.values()))
print(O)