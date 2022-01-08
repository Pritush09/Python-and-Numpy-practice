list1 = [1,2,3,4,5]
# then list can take any kind of datatype like int , dictionary , tuple , set and a list itself

# all the element ont it has an index which start over from zero like the orange int list has index zero and 2 is 1
# we can access the element by there index
print(list1[1])

# we can also do slicing of list
print(list1[0:2])
# we can also do advance slicing in the list
print(list1[0::2])

# list are also iterable means that we can access the element one by one with the
# # now checking out some functions of list
#
# # 1. if we want to add an  element to the list
list1.append(8)

# # 2. if want to insert an element at a particular index
list1.insert(2,4)
# it takes first value as an index and second vlaue as an element help of the loop which we will do later on

# 3. if we want to sort a list in ascending order ## applicableonly when whole list is integer or a float\
list1.sort()
# to reverse
list1.reverse()

# 4. if we want to remove a particular element from the list
list1.remove(8)

# 5. if we want to remove the last element then
list1.pop()

print(list1)


