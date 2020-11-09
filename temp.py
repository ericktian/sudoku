# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # temp = [0]*7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # temp[6] = 3
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(len(temp))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(temp)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # input = sys.argv[1]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # input = input.replace('.', '0')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(input)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # pzl = int(input.split(''))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(pzl)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # import sys
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # input = sys.argv[1]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # input = input.replace('.', '0')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # pzl = []
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(0, len(input)):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     pzl.append(int(input[i]))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(pzl)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # pzl = [1, 2, 3, 1, 2, 1, 4, 5, 6, 4, 5, 1, 2, 6, 3, 1, 2, 3, 6, 2, 4, 5, 4, 6]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # def temp(pzl):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     numcounts = [0] * 7
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     for i in pzl:
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         numcounts[i] += 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     curr = numcounts[1]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(numcounts)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     for i in range(1, len(numcounts)):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         if numcounts[i] != curr: return False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     return True
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(temp(pzl))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print(len('ABCABCDEFDECFABCABFDEFDE'))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # print('123123456453612312645645')
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # list = [0, 0.981, 1.445, 1.790, 1.988, 2.546, 2.653, 2.681, 2.878]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # delta = .1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # for i in range(1, len(list)):
# # # # # # # # # # # # # # # # # # # # # # # # # # # #     print(i, ":", "\nforce of gravity:", .001*i*9.81, "\n", "velocity^2:", list[i]**2, "\n",
# # # # # # # # # # # # # # # # # # # # # # # # # # # #           "error:", 2*list[i]*delta+delta**2, -2*list[i]*delta+delta**2)
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # pzl = [9, 1, 3, 2, 4, 0, 4, 2]
# # # # # # # # # # # # # # # # # # # # # # # # # # # setp = set(pzl)
# # # # # # # # # # # # # # # # # # # # # # # # # # # setp.remove(0)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(setp)
# # # # # # # # # # # # # # # # # # # # # # # # # # # print(9 - len(setp))
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # setp = set([pzl[i] for i in lookupset[n]])
# # # # # # # # # # # # # # # # # # # # # # # # # # setp.remove(0)
# # # # # # # # # # # # # # # # # # # # # # # # # list = [0, 0.981, 1.445, 1.790, 1.988, 2.546, 2.653, 2.681, 2.878]
# # # # # # # # # # # # # # # # # # # # # # # # # delta = .1
# # # # # # # # # # # # # # # # # # # # # # # # # for i in range(1, len(list)):
# # # # # # # # # # # # # # # # # # # # # # # # #     print(i, ":", "\nforce of gravity:", .001*i*9.81, "\n", "velocity^2:", list[i]**2, "\n",
# # # # # # # # # # # # # # # # # # # # # # # # #           "error:", 2*list[i]*delta+delta**2, -2*list[i]*delta+delta**2)
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # setx = set(i for i in range(100) if i%10==0 or (i+1)%10==0)
# # # # # # # # # # # # # # # # # # # # # # # # print(setx)
# # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # sety = set(range(0, 100, 10)).union(set(range(9, 100, 10)))
# # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # dict = {i: {j for j in range(10) if (j+i)**.5%1==0} for i in range(10)}
# # # # # # # # # # # # # # # # # # # # # # # print(dict)
# # # # # # # # # # # # # # # # # # # # # # # dict = {i: {j for j in range(10) if (j+i)**.5%1==0} for i in range(10)}
# # # # # # # # # # # # # # # # # # # # # # # print(dict)
# # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # numberPositions = [0]*10
# # # # # # # # # # # # # # # # # # # # # # for i in range(len(numberPositions)):
# # # # # # # # # # # # # # # # # # # # # #     numberPositions[i] = set()
# # # # # # # # # # # # # # # # # # # # # # print(numberPositions)
# # # # # # # # # # # # # # # # # # # # # # numberPositions[2].add(3)
# # # # # # # # # # # # # # # # # # # # # # print(numberPositions)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # n = 9
# # # # # # # # # # # # # # # # # # # # # s = 53
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # print(s//n * n)
# # # # # # # # # # # # # # # # # # # # # print((s+n)//n * n)
# # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # list1 = [i for i in range(n**2) if((i > s//n * n and i < (s+n)//n * n) or (s%n == i%n)) and i != s]
# # # # # # # # # # # # # # # # # # # # # print(list1)
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # n = 9
# # # # # # # # # # # # # # # # # # # # s = 53
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # list1 = [[i for i in range(n**2) if i+1 == s or i-1 == s or i+n == s or i-n==s] for s in range(n**2)]
# # # # # # # # # # # # # # # # # # # # print(list1)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # [set(i for i in range(len(cl)) if k in cl[i]) for k in range(mx)]
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # [set.union(i for i in cl if k in i) for k in range(mx)]
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # game = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # # # # # # # # # # # # # # # # xlate = [i for i in range(len(game))]
# # # # # # # # # # # # # # # # # # newGame = [game[i] for i in xlate]
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print(game)
# # # # # # # # # # # # # # # # # # print(xlate)
# # # # # # # # # # # # # # # # # # # print(newGame)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # xlate1 = [len(game)-i-1 for i in xlate]
# # # # # # # # # # # # # # # # # # # print(xlate1)
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # xlate2 = [int(i//(len(game)**.5)*len(game)**.5 + (len(game)**.5 - i%len(game)**.5 - 1)) for i in xlate]
# # # # # # # # # # # # # # # # # # # print(xlate2)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # xlate3 = [int(i//(len(game)**.5) + len(game)**.5*(i%(len(game)**.5))) for i in range(len(game))]
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # xlate3 = [int(len(game)**.5-1-i//(len(game)**.5) + len(game)**.5*(i%(len(game)**.5))) for i in xlate]
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # xlate4 = [(len(game)-1+i)%len(game) for i in range(len(game))]
# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # print(xlate4)
# # # # # # # # # # # # # # # # # # # print(xlate3)
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # n = 10
# # # # # # # # # # # # # # # # # # list1 = {i:{j**2-i for j in range(int((i+n)**.5+1))  if j**2-i>0} for i in range(n+1)}
# # # # # # # # # # # # # # # # # list1 = [(i, j) for i in range(1, n+1) for j in range(n, int(n**.5)-1, -1) if int((i+j)**.5)==(i+j)**.5 and i!=j]
# # # # # # # # # # # # # # # # # print(list1)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print({j for j in range(0, 100, 10)})
# # # # # # # # # # # # # # # # # val1, val2 = "something", "else"
# # # # # # # # # # # # # # # # # print(val1)
# # # # # # # # # # # # # # # # # print(val2)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # templist = [5 if i%5 == 0 else 7 if i%7 == 0 else i for i in range(1, 101)]
# # # # # # # # # # # # # # # # # print(templist)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print({i for i in range(10) if i**.5%1!=0})
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # pzl = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'
# # # # # # # # # # # # # # # # print(''.join([pzl[i*9:i*9+9] + '\n' for i in range(9)]))
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # lstNums = [1, 2, 3, 4]
# # # # # # # # # # # # # # # sm = sum(lstNums[j] for j in range(len(lstNums)))
# # # # # # # # # # # # # # # print(sm)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # temp = [7]*20
# # # # # # # # # # # # # # print(temp)
# # # # # # # # # # # # # # print(len(temp))
# # # # # # # # # # # # #
# # # # # # # # # # # # # temp = {i for i in range(99) if i%10 == 0 or i%10 == 8}
# # # # # # # # # # # # # print(temp)
# # # # # # # # # # # #
# # # # # # # # # # # # myStr = 'asdfasd'
# # # # # # # # # # # # temp = list(set(list(myStr)))
# # # # # # # # # # # # print(temp)
# # # # # # # # # # #
# # # # # # # # # # # temp = ''.join(["frog"]*9)+"toad"
# # # # # # # # # # # print(temp)
# # # # # # # # # #
# # # # # # # # # # pzl = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'
# # # # # # # # # # for idx in range(len(pzl)):
# # # # # # # # # #     sym2 = pzl[idx]
# # # # # # # # # # print(sym2)
# # # # # # # # # # sym = pzl[len(pzl)-1]
# # # # # # # # # # print(pzl)
# # # # # # # # # # print(sym)
# # # # # # # # #
# # # # # # # # # print([5 if i%5 == 0 else 7 if i%7 == 0 else i for i in range(1, 101)])
# # # # # # # #
# # # # # # # # print({i for i in range(1024) if i**.5%1!=0})
# # # # # # #
# # # # # # # pzl = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'
# # # # # # # print("".join([pzl[i*9:i*9+9] + '\n' for i in range(9)]))
# # # # # #
# # # # # # pzl = '417369825632158947958724316825437169791586432346912758289643571573291684164875293'
# # # # # # temp1 = []
# # # # # # for idx in range(len(pzl)):
# # # # # #     temp1.append(pzl[idx])
# # # # # # print(temp1)
# # # # # # temp2 = []
# # # # # # for i in [pzl[j] for j in range(len(pzl))]:
# # # # # #     temp2.append(i)
# # # # # # print(temp2)
# # # # # # # print(set(list(range(0, 100, 10))))
# # # # # # # print([j for j in range(0, 100, 10)])
# # # # #
# # # # # binInt = 100101
# # # # # temp = int(str(binInt), 2)
# # # # # print(temp)
# # # # # temp2 = str(binInt)
# # # # # for i in range(len(temp2)):
# # # # #     if temp2[i] == '1':
# # # # #         print(len(temp2)-1-i)
# # # # # def ind():
# # # # #     return next((x for x in [len(str(binInt)) - 1 - i if str(binInt)[i]=='1' else -1 for i in range(len(str(binInt)))] if x > -1), None)
# # # # # # def ind():
# # # # # #     for i in range(len(str(binInt))):
# # # # # #         if str(binInt)[i]=='1': return len(str(binInt))-1-i
# # # # # print(ind())
# # # #
# # # # xlate = [*range(64)]
# # # # print([int((i//8)*8+(7-i%8)) for i in xlate])
# # #
# # # print(len('[5 if i%5==0 else 7 if i%7==0 else i for i in range(1,101)]'))
# # # print(len('[(j if j%7 else 7) if j%5 else 5 for j in range(1,101)]'))
# #
# print(len('{i for i in range(1024) if i**.5%1!=0}'))
# print(len('{*range(1024)}-{j*j for j in range(32)}'))
# print({i for i in range(1024) if i**.5%1})
# print({*range(1024)}-{j*j for j in range(32)})
# #
# #
# # print(len('print("an".join([pzl[i*9:i*9+9] for i in range(9)]))'))
# # print(len('print(“\n”.join([pzl[j:j+9] for j in range(0,81,9)]))'))
# #
# # pzl = '814976532.5.123478.3.854169948265317275341896163798245391682754587439621426517983'
# # print("\n".join([pzl[i*9:i*9+9] for i in range(9)]))
# # print()
# # print("\n".join([pzl[j:j+9] for j in range(0,81,9)]))

print([[0]*9]*9)