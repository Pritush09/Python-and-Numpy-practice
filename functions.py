# the functions contains a program which we gonna use in our codes very often
# due to which we dont have to write the same code repeated number of times
# we will just call the reqired function which will serve rhe same

# there are several in built functions which are defined in python itself
# like sum() , len() , type() etc

# but we can  define our function  which will help in serving more difficult task also
# and the functions can also take input in different forms and different ways
a = 2
d = 3
def average(a,d):
    """Return the average of the two given numbers"""
    # this above is the doc string which is used to keep the short and consice detail
    # about what task is performed by the function
    f = 9
    average1 = a+d/2
    return average1

#average(2,3)   # this will not give an output like this we have to store it in a variable

n = average(a,d)     # then print the return value
print(n)
#  we access the doc string by
print(average.__doc__)

# ##### Dont ever use call the function before defining it

# it is always preferred to keep our function short and consice to proper understanding
# of  the given code inside the function


# the variable which we define inside the function is called local variable which the
# other function can not access like f = 9

# the variable like a and d are  global variable which can be access by all the function
# in the programme



