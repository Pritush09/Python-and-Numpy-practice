import numpy as np

stat12 = np.array([[1,2,3],[4,5,6]])
print(stat12)
print('\n')
# Finding the minimum of the given data
min = np.min(stat12)
print(min)
print('\n')

# Use of axis in finding min
min2 = np.min(stat12,axis=1)   #this will give me the min of the 1st row and the min of the 2nd row
print(min2)
min3 = np.min(stat12,axis=0)  #this will give the result column wise
print(min3)
print('\n')

# Use axis in finding max
max = np.max(stat12,axis=0) # column wise deta he
print(max)
max1 = np.max(stat12,axis=1) # row wise deta he
print(max1)
print('\n')

# other calculation purposes of numpy
sum1 = np.sum(stat12)
print(sum1)
print('\n')
sum2 = np.sum(stat12,axis=0)   #ye column wise print karta he
print(sum2)
print('\n')
sum3 = np.sum(stat12,axis=1)  # ye row wise print karta he
print(sum3)
print('\n')

#       Reorganizing array
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print('\n')

after = before.reshape(8,1)     #isme self , shape , order
print(after)           #if it shows error it will because the element does not fit in that shape
print('\n')

# vertical stacking vectors
n1 = np.array([1,2,3,4])
n2 = np.array([5,6,7,8])

vertical_stack = np.vstack([n1,n2,n2,n1])    #ye only one argument hi leta he   # u can also repassing it
print(vertical_stack)                        # it will show error if the rows are mismatch
print('\n')

# Horizontal stacking vectors
h1 = np.zeros((2,4))                         #rows equal hona chahiye warna error hoga
h2 = np.ones((2,2))
horizontal = np.hstack([h1,h2])
print(horizontal)
print('\n')











