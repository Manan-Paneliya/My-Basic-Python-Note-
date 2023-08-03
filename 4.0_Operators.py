### Operators in python ###
## Types of Operators ##
'''
(1) Arithmetic Operators - +,-, / , * , % , // , **
(2) Comparison Operators - > , < , == , != , >= , <=.
(3) Logical Operators    - and , or , not
(4) Assignments Operators- += , -= , /= , *= , %= , //= , **=
(5) Identity Operators   - is , is not
(6) Membership Opreators - in , not in
(7) Bitwise Operator     - & , | , ^ , ~ , << , >> .
'''
print("'\n'********************************** Arithmetic Operators *********************************''\n'")
# Arithmetic Operators
print(23 + 34)
print(34 - 76)
print(45 / 5)
print(78 * 2)

print('********************************** Comparison Operators *********************************')
# Comparison Operators
if 12 > 2:
    print('grater')

print('********************************** Logical Operators *********************************')
# Logical Operators
a = 2
b = 3
c = 2
print((a and b) == c)  # a and b both are equal to c or both are not
print((a or b) == c)  # a or b , any one are equal to c
print(not a)  # a are False , simply it inverse

print('********************************** Assignment Operators *********************************')
# Assignment Operators
a += 2  # it means a = a + 2)      # similarly With All Assignment Operators

print('********************************** Identity Operator *********************************')
# Identity Operator
a1 = 3
b1 = 3
a2 = 'python'
b2 = 'python'
a3 = [4, 5, 6]
b3 = [4, 5, 6]

print(a1 is not b1)
print(a2 is b2)
print(a3 is b3)  # List are not Identical, therefor it is False .
print('********************************** membership Operator *********************************')
# membership Operator
l1 = [1, 4, 'python', 3, 9.02]
print(4 in l1)  # it prints true if 4 is present inside l1, otherwise print False
print('pytho' in l1)
print(9.02 not in l1)  # ti tells 9.02 is not present inside l1 when it is Wrong it Print False

