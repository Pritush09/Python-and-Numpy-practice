# firstly we will store the string in a variable
# done this in pycharm so have to print statement every time not in jupyter

var1 = "Pritush is @ so good"

# firstly started with slicing
print(var1[::])

# default value of the first part and the last part of var1[::] is one
# for the first value 1 means that it it will start with the first element
# the last means it will have the interval of one
# the middle one is for the last element till where we want to iterate through the string

print(var1[1:9:2])

print(var1[:90:6])

print(var1[:10]) # if there is only one semicolumn then first means the same and last one means as the middle in the above

print(var1[::90])

# Negative slicing
print(var1[-4:]) #it start from the given index and goes forward
# this can be written as
print(len(var1)) # checking the lenght of the string
print(var1[14:])

# now running some functions of string
print(var1.isalnum()) #this gives boolean vallue false as the string is not a alpha numeric(@$)

print(var1.isalpha()) # this will also give false as the string does not fully contains alphabet it also contains alpha numeric

print(var1.endswith("good")) # this check whether the given string endswith the given argument good true in this case

print(var1.count("o")) #this tell us how many time the given argument appears in the string

print(var1.capitalize()) # this capitalizes the first element of the given sstring

print(var1.lower()) # this will lowercase the given strring

print(var1.upper()) # this will uppercase the given string

print(var1.find("good")) # this return the index from where the given argument is starting in the string

print(var1.replace("@","_")) # this will replace the fir argument from the string with the second argument