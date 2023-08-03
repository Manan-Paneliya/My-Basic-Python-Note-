# recursion : recurive VS iterative Approch

def factorial_iterative(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print(f)

def factorial_recursive(n):
    if n == 1 :
        return 1
    else:
        return n * factorial_recursive(n-1)

inp = int(input("Enter a Number : "))
it = factorial_iterative(inp)
r = factorial_recursive(inp)
print("Factorial using factorial_iterative : ",it)
print("Factorial using factorial_recursive : ",r)

# Make Fibonacci series using recursive
def fibo(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)
ind = int(input("Enter a Value : "))
print(fibo(ind)) 

# calculate a sum up to Number using recursive method
def sum(n):
    if n==0:
        return 0
    elif n==1:
        return 0+1
    else:
        return n + sum(n-1)
inp2 = int(input("Enter a Number for sum upto n : "))
print(sum(inp2))

''' recursive method :-
                       --  it is complex compare to iterative 
                       -- there is a problem of debuging
                       -- less line of code compare to iterative.'''
''' iterative method :-
                       -- code is simple
                       -- no any problem of debuging '''

