### ITERAVITE APPROACH
# finding the factorial using iterative approach

def factorial_iterative(n):
    """parameter : n (Integer)
       return: n*(n-1)*....*1 """
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac

y = int(input("Enter the number for which u want the factorial: "))
print(factorial_iterative(y))


#####  Recurssicve approach
# this is for the factorial of the given number
def recur(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n*recur(n-1)

yi = int(input("Enter the number: "))
print(recur(yi))


# for fibonacchi series
def recur_fibo(n):
    if n == 0:
        return 0
    elif n== 1 or n==2:
        return 1
    elif n>2:
        return recur_fibo(n-1)+recur_fibo(n-2)

yio = int(input("Enter the number for fibo: "))
print(recur_fibo(yio))

