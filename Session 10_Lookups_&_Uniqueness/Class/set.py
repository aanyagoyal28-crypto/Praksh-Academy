'''
set - unchangable, unique, unordered and unindexed collection of data

syntax : variable_name ={}

'''

set_1 = {1,2,3,4,5,6,7,1,2,3,4,5,6,7}
# print(len(set_1))

# list1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
# set_2 = set(list1)
# print(list1)
# list1=list(set_2)
# print(list1)

# for i in set_1:
#     print(i)


# set_1.add(8)
# set_2 = {9,10,11,12,13,14,15}
# set_1.update(set_2)
# print(set_1)

# list_1 = [16,16,16,16,16]
# set_1.update(list_1)
# print(set_1)

# # set_1.remove(20)
# set_1.discard(14)
# print(set_1)

# set_1.pop()
# print(set_1)

# set_1.clear()
# print(set_1)

# del set_1
# print(set_1)


# set_1 = {1,2,3,4,5,6,7}
# set_2 = {5,6,7,8,9,10}
# set_4 = {11,12,13,14,15}
# set_5 = {16,17,18,19,20}
# set_3 = set_1.union(set_2,set_4,set_5)
# # set_3 = set_1 | set_2 | set_4 | set_5
# print(set_3)

# tuple_1=(5,6,7,8,9,10)
# # set_6 = set_1.union(tuple_1)
# set_6 = set_1 | tuple_1 #symbol union operator it can only join two set's if you have to join tuple and a set you need to use union operator
# print(set_6)


set_1={'red','green','blue','yellow','orange'}
set_2={'purple','pink','brown','black','white','orange','red'}
# set_3 = set_1.intersection(set_2)
# set_3 = set_1 & set_2
# print(set_3)

# set_3 = set_1.difference(set_2)
# set_3 = set_1 - set_2
# print(set_3)

set_3 = set_1.symmetric_difference(set_2)
print(set_3)

frozen_set = frozenset(set_1)
print(frozen_set)
frozen_set.add('violet') #frozen set is immutable so we cannot add or remove any element from it