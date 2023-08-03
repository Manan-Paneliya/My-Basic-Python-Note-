x = int(input("Enter a number : "))
y = int(input("Enter a number : "))
o = input("Enter a String : ")
o = o.replace(" ", "")
if o == "+":
    print("Addition : ",x+y)
elif o == "*":
    print("Multioplication : ",x*y)
elif o == "/":
    print("Division : ",x/y)
elif o == "-":
    print("Substraction : ",x-y)
else :
    print("Invalid Operator ")
