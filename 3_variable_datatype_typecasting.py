# Variable

var1 = 'Jay Swaminarayan'  # var1 is a variable
var2 = 4
var3 = 34.9
print(var1, '\n', var2, var3)
print('********************************** 1 **********************************')

# Type 
print(type(var1))  # it ask which type of character is "var1".
print(type(var2))
print(type(var3))
print('********************************** 2 **********************************')

# Concating (means adding of variable)
var4 = " Hari"
print(var1 + var4)
print(var2 + var3)
''' print(var4 + var2)'''  # it gives error
print('********************************** 3 **********************************')

# Type Casting 
var5 = "50"
var6 = " 50"  # it is a String as a number
var7 = "Hari"
print(var5 + var6)
print(int(var5) + int(var6))  # int() convert enyone into integer
'''print(int(var7))'''  # it is not possible
print(float(var5))
print(str(var5))
print(10 * 'Jay Swaminarayan\n')
print('********************************** 4 **********************************')

# Take Input from user
a = input('enter : ')  # it takes any type of value int,float,str,complex .
b = input("Enter : ")  # also write like this
print(a, b, '\n', int(a) + int(b))

c = int(input('enter any number:'))  # it input only number
d = float(input('enter any float number:'))  # it input only float
e = str(input('enter characters:'))  # it input only string
print(c + d)
