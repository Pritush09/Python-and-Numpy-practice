import numpy as np
n = np.array([1,2,3,4,5,6,7,],dtype="int8")
#data type
b=n.dtype
print(b)
#get dimensions
m=n.ndim
print(m)
o=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(o)
d=o.ndim
print(d)
#get the shape
s=o.shape
print(s)
#jese 2 row he aur uske andar 3 column he
#get the item size
j=n.itemsize
print(j)
jp = o.itemsize
print(jp)
#the total no. of element
h=o.size
print(h)
#get the total size
f=o.nbytes
print(f)

print("------------------------------------------------------------------------------------------------------------")

ar=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(ar)
jh=ar.shape
print(jh)

#get the specific element * remember python indexing always starts with zero
k=ar[1,5]
print(k)


#geting a spesific row
row=ar[0,:-3]
print(row)


#comma khel he


#get the specific column
column=ar[0:,2]
print(column)

#little bit fancy [startindex:endindex:stepsize] yaha zero matlab start kaha se karnn he
slicing=ar[0,1:6:2]
print(slicing)


#if u want the replace the array
ar[1,5]=20
print(ar)
#if u want to insert by replacing that one in column
ar[:,2]=[1,2]
print(ar)



# 3D Example
threeD=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(threeD)

#get the specific element (work outside in)
var1=threeD[0,1,1]
print(var1)

var2=threeD[:,1,:] #colum wala he yeh
print(var2)

#practice wala he ye
array1= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[9,8,7,3]]])
print(array1)
slice1=array1[1,:1:]
print(slice1)


print('---------------------------------------------------THE END--------------------------------------------------------------------')





