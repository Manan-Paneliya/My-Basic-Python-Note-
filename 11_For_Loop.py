### Loops ###
''' there are two types of loop
    1) While loop : it continue the executiom of loop until the iterable(list,tuple,dictionary) was complete.
    2) For loop : in which we can put a condition.
                 it continue the execution of loop until the condition is true
'''
# for loop
print('for loop')
print('********************************** Example 1 *********************************')
# for example
a = ['harrry', 'carry', 'darry', 'larry']
for i in a:
    print(i + ' is good Boy')  # it Print all iterable of list one by one

print('********************************** Example 2 *********************************')
# for example
l2 = (('harry ', '1kg'), ('larry', '2kg'), ('carry', '5kg'), ('elephant', '500kg'))
for person, eat in l2:
    print(person, 'eats every Day ', eat)

'''in this example :
                    first it takes first element and add Given string between them 
                    and take second element ......so no up to last element'''

## While loop : in this we put a condition , loop are continue yet condition are true
print('********************************** Example 3 *********************************')
# for example
n = 0
while n < 5:  # it will rotate the loop until the value of 'n' is 5 or more than 5.
    print('while')
    n = n + 1
