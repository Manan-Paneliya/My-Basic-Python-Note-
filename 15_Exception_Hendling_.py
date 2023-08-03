# Exeption and Handling
''' exception : an exception is an error which
                occurs during the exception of
                a program .

              : it is also called run time error or logical error . '''
# their are 2 types of exception
#(1) built-in exception
#(2) user-define exception
'''
example of built-in exception 
1) Exception
2) ZeroDivisionError    
3) NameError
4) TypeError
5) ValueError
6) IOError .....etc  '''

# Exception handling Mecanism

''' 
try:
----statement where 
    exception is likely 
    generate
except:
---- ___________
     ___________
     ___________
'''
'''A programming language Which provide axception handling  is called Roburst programming language '''
# example
''' if we make a program of division of 2 number , and we divide 5 with 0 , then it gives ERROR 
    we can handle this problem by exception by exception handling .'''

# the below code in comment gives error when we any number by 0
# for example
'''
a =int(input("enter a First number : "))                
b =int(input("enter a second number : "))
c = a/b
print("division : ",c)                     '''

# we gives ZeroDivisionError in the above code
# so we handle this problem
try:
    a =int(input("enter a First number : "))
    b =int(input("enter a second number : "))
    c = a/b
    print("division : ",c)

except ZeroDivisionError :
    print("you cannot divide a number with zero")

# when multiple exception are present in a single try block , we can put the name of exception.
# like this below
'''
except EcxeptionName:
     print("you cannot divide a number with zero")
'''

# another syntex of ecxeption handling

'''
try:
  ____________
  ____________
  ____________
except ExceptionName1 , ExceptionName2 , ...:
    ____________
    ____________
    ____________

except ExceptionName3 , ExceptionName4 , ...:
    ____________
    ____________
    ____________

except ExceptionName5 : 
    ____________
    ____________
    ____________
except:                # this are work as "else"
    ____________
    ____________
'''
