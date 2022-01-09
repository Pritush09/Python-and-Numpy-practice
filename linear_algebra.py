import numpy as np

# Multiply the two matrices array
a = np.ones((3,2))    # pehle wala ka jitna column he durse wala ka utna row hona chahiye
b = np.full((2,3),3)    #pura normal matrices ki tarah he
multiply_karlo_friends = np.matmul(a,b)
print(multiply_karlo_friends)


print('\n')

#  Finding detrminant of matrices
c = np.identity(3)
print(c)
value_of_determinant = np.linalg.det(c)
print(value_of_determinant)
print('\n')

print('for more go to the give web in the free code camp video')

print('---------------------------------------------THE END----------------------------------------------')



