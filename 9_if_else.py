### If & Else : it is used to execue code acording to conditon that we input

v3 = int(input('enter any value :'))
''' if block : if your condition is true then it executes statement of their block
             : it is not mandatory to take else block'''
'''if-else block : if your condition is true inside "if" block it execute ststement of "if" block,
                   otherwise it switch to the else block'''
'''if-else with elif block  : if your condition is true inside "if" block it execute ststement of "if" block,
                              otherwise it switch to the elif block and when it is false it switch to next elif block , and so no. '''

print("'\n'********************************** If block *********************************''\n'")
# if block
if v3>50:
      print("grater")

print("'\n'********************************** if-else block *********************************''\n'")
# if-else Block
if v3>0:
    print('positive integer')
else:
    print('negative integer or zero')

# if-else Block with elif (use for put multiple condition)
print("'\n'********************************** if-else block with elif *********************************''\n'")

v4 =int (input('enter your marks:'))
if v4>100:
    print('your mark is invalid')
elif v4>90:
    print('A+ Grade')
elif v4>80:
    print('A Grade')
elif v4>70:
    print('B+ Grade')
elif v4>60:
    print('B Grade')
elif v4>50:
    print('C Grade')
elif v4>40:
    print('D Grade')
elif v4>=33:
    print('E Grade')
else :
    print(' you are Fail')



