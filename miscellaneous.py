import numpy as np
# Miscellaneous
# Load data from files
filedata = np.genfromtxt("main.txt",delimiter=',')                #delimeter matlab kise tum sepearate karoge
print(filedata)
print('\n')
filedata2 = filedata.astype('int32')        #we can change the datatype of it           # it takes in self , dtype , order , casting , subook , copy
print(filedata2)        # astype makes a copy of the the given data
print('\n')


#  Boolean masking and Advanced Indexing
checking_bool = filedata2 > 50         # gives according to that particular value
print(checking_bool)
print('\n')
#  we can use axis to determine the checking of the bool
checkbool = np.any(filedata > 9, axis=0)                      # yaha par bhi 0 he matlab column aur 1 toh row wise he he
print(checkbool)
print('\n')

geting_particular_value = filedata[filedata > 9]     # u can the list of a particular value by doing this
print(geting_particular_value)
print('\n')
# U can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
aindex = a[[1,2,8]]              # always keep in doble bracket
print(aindex)

#################### Check the screenshots in your mobile phone for the last part

print('-----------------------------------------------------THE END--------------------------------------------------------------------')

























