# if we want to take decisions based on comparision of two or three or many more
# parameters we have to use if else statement ladder to achieve it

var1 = 65
var2 = 56
var3 = int(input("Enter the number: ")) # this input statement is used to take input
# from the user and as it take the input in the form string and we are comparing it with
# integers we have to convert it in int data type using int() function

if var3>var1:
    print("Grater")
elif var3<var2:
    print("lesser")
elif var3== var2:
    print("equal to 56")
elif var3 == var1:
    print("equal to 65")
else:
    print("middle")
# this space in the next line after semicolon is called indentation which denotes that
#  it is the body of that heading of the statement whether it be if or else anad will
# only executed if the statement is true

# it is like basic conversation like if this then do this else do this

# We can also use this for the list also
l = [1,2,2,3,4,5,6,9,8,7]
nin = int(input("Enter the number for which u wanna check for: "))
if nin in l:
    print("Yes in the list")
else:
    print("not in the list")


# Guess the number game with this basic if else statement
n = 18
n1 = int(input("Enter the number u guess: "))
if n1 == n:
    print("You nailed it")
elif n1> n:
    print("try again with lesser number")
else:
    print("try again with larger number")



