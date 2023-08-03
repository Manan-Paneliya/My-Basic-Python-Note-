# Functions in Python
# there are built-in and user-mad functions
# we learn to make function
import math
# we use def function to make function
# syntex of def()
''' def name(argument):
    ----statement
    ----statement
      
        return value  

   name(parameter)    '''    # to use the function
print('********************************** 1 **********************************')
# make a function to sum of 2 number

def sum(x,y):
    a = x + y
    return a   # return is a best practice rather than print()
print(sum(5,8))

print('********************************** 2 **********************************')
# a function without argument or parameter
def js():                     # this function only print "Jay Swaminarayan" .
    print("Jay Swmaminarayan")

js()
print('********************************** 3 **********************************')
# make a function to square of a number
def sqr(n):
    return n**2
print(sqr(3))

print('********************************** 4 **********************************')
# make a function to average of three numbers
def avg(a,b,c):
    return (a+b+c)/3

print(avg(1,2,3))

print('********************************** 5 **********************************')
# Docstring in Function
''' large number of functions and their name are not possible to mind , 
    so , builder of function put string (as a advise that what is work of their function ) in the 
    their function is called DocString. and user able to see the DocString of perticular function .'''
# for example
def mul(x,y):
     """this function is multiplies the 2 number """  # this is a docstring of mul()
     return (x * y)
print(mul.__doc__)         # print the docstring of mul()
print(mul(3,5))

print('********************************** 6 **********************************')
# examle 2
def avg4(a,b,c,d):
    """This Function is calculate the average of 4 number """
    return (a+b+c+d)/4

print(avg4.__doc__)
print(avg(1,2,3))
print(math.radians.__doc__)  # doc String of pre-define
