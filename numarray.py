#initializing different types of arrays
import numpy as np
#creating a array of only zeros
zeros=np.zeros((2,3,3,2)) # 2 row 3 column 3 row 2 column
print(zeros)

# All ones matrix
ones = np.ones((4,2,2,3),dtype='int32')# 4 big rows 2 big column 2 small rows and 2 columns
print(ones)

print('\n')

#for any other no.
any_num = np.full((2,2),99)# pehle leta he shape fir leta he number
print(any_num)

print('\n')

#for any other using full_like
full2 = np.full_like(ones, 3)# U can use previous format by mentioning it  #this take shape,dtype,no. of which u want to build the np of
print(full2)
print('\n')


# For geting a random decimal no.
random = np.random.rand(4,2) #In this no internal bracket is reqired like (())
print(random)
print('\n')

#if you want to pass in the shape in above
pass_shape = np.random.random_sample(ones.shape)
print(pass_shape)
print('\n')

#getting a random integer value
integer_val=np.random.randint(1,3,(4,4),dtype='int16')  #this function takes low , high , size , datatype
print(integer_val)
print('\n')

#printing an indentity matrix
identmatrix = np.identity(6,dtype='int64')
print(identmatrix)
print('\n')

#If u want to repeat an array for a specified no. of times
arr = np.array([[[1,2,3]],[[4,5,6]]])   #if the vector is 3 dimensional then 2 axis are allowed and same apply for rest of the all
r1 = np.repeat(arr,3,axis=2)        #baki sab khud karke dekhlo
print(r1)
print('\n')

#Task
# [1,1,1,1,1]
# [1,0,0,0,1]
# [1,0,9,0,1]
# [1,0,0,0,1]
# [1,1,1,1,1]

ore = np.ones((5,5))
print(ore)
zer = np.zeros((3,3))
print(zer)
zer[1,1] = 9
print(zer)
ore[1:4,1:4] = zer # row or column hota he pagal
print(ore)
print('\n')

print("----------------------------------------------------THE END------------------------------------------------------")

print('\n')


"""
                       BE CAREFULL WHEN COPYING ARRAYS!!!
"""
# Copy the array before using it in another one
a = np.array([1,2,3])
b =a.copy()
b[0] = 12
print(a)
print('\n')

DIV = a/2
print(DIV)

f= b+a
print(f)

#take sin , cos and everything
d = np.cos(a)
print(d)
















