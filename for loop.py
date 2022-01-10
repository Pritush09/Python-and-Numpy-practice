# this is usually used to unpack the elements from iterable type of datatype
# basically help in iterating through the elements of the iterable datatype

# firstly list
lsi = ["harry","larry","page","cage","gen","fan"]

# ffirstly we can access the elements via this
print(lsi[0],lsi[1],lsi[3])

# but if there are like 1000 elements in the list it is practically not good to write
# all the elements like that in that case we sue loop
for i in lsi:
    print(i,end=' ') # the end part help us to define how the next element
    # would be printed after the first one
print("\n")

lis= [["harry",1],["larry",2],["page",3],["cage",4],["gen",5],["fan",6]]
print(lis[0])

# convert this to dict then iterate through it
d = dict(lis)
print(d)
for i in d:
    print(i,end=" ") # this will return the key of the dictionary
    print(d[i],end=" ") # this will return values of the keys from the dictionary
print("\n")

# with this we can also change the elements as we iterate through them
# so it has very much importance in coding



