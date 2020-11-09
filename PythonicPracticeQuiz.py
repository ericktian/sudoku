# #A
# A = {10*j for j in range(10)}
# A1 = {*range(0, 91, 10)}
# print('A', A)
# print('A1', A1)
# #B
# myDct = {"myKey": 0}
# B = myDct.get("myKey")
# B1 = myDct["myKey"]
# print('B', B)
# print('B1', B1)
# #C
# val1 = 1
# val2 = 2
# temp = val1
# val1 = val2
# val2 = temp
# valA = 1
# valB = 2
# valA, valB = valB, valA
# print('val1', val1, 'val2', val2)
# print('valA', valA, 'valB', valB)
# #D
# sn2 = 2
# sn = 3
# symNum = 2
# for i in range(1):
#     print(sn2 == sn or sn2 == symNum)
#     if sn2 == sn or sn2 == symNum: continue
#     print('here')
# for j in range(1):
#     print(sn2 in [sn2, symNum])
#     if sn2 in [sn2, symNum]: continue
#     print('here2')
# #E
# myNum = 27
# if myNum==27: print('false')
# else: print('true')
# print(myNum!=27)
# #F
# myKey = 'key'
# myDct = {myKey: '0'}
# if myKey not in myDct.keys(): print('true')
# if myKey not in myDct: print('true')
#G

#other
# pzl = '814976532.5.123478.3.854169948265317275341896163798245391682754587439621426517983'
# print({*pzl})
# tempset = {1, 2, 3}
# print(tempset.pop())
# print([j for j in [2, 7, 9] if not 49%j])
# print([i for i in range(10, 101) if not [j for j in [2, 7, 9] if not i%j]])
#
# for i in 0:
#     if 0 in [0,1]:continue


# add()	Add an element to a set
# clear()	Remove all elements form a set
# copy()	Return a shallow copy of a set
# difference()	Return the difference of two or more sets as a new set
# difference_update()	Remove all elements of another set from this set
# discard()	Remove an element from set if it is a member. (Do nothing if the element is not in set)
# intersection()	Return the intersection of two sets as a new set
# intersection_update()	Update the set with the intersection of itself and another
# isdisjoint()	Return True if two sets have a null intersection
# issubset()	Return True if another set contains this set
# issuperset()	Return True if this set contains another set
# pop()	Remove and return an arbitary set element. Raise KeyError if the set is empty
# remove()	Remove an element from a set. If the element is not a member, raise a KeyError
# symmetric_difference()	Return the symmetric difference of two sets as a new set
# symmetric_difference_update()	Update a set with the symmetric difference of itself and another
# union()	Return the union of sets in a new set
# update()	Update a set with the union of itself and others

# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list


# x = [(x%5 and (x%7 and x or 7)) or 5 for x in range(1, 101)]
#
# print(x)












#