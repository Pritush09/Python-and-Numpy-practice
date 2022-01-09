set1 = {1,2,3,3,4,5,6,6,67}
print(type(set1))
print(set1) # here only one 3 and 6 would be taken
# the sets only contains the uniqe values and automatically removes the same ones
# out of the set


# these are mutable and iterable(using loops)

# if wanted to add an element to the list
set1.add(8)  # u can only add one element only at one time
# and also not list of element here
print(set1)

set2 = {1,2,3,4,99,0,88,98}

### Now we can perform deferent type of set functions just like in mathematics

print(set1.union(set2)) # gives same result as in the mathematics

print(set1.intersection(set2))

print(set1.isdisjoint(set2)) # this tells us whether the elements in the given set1
# is different from the elements of set2





