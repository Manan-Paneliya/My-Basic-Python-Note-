'''
construct a pattern
*
**
***
****    # if boolean is True and n number of rows.

or construct a inverse pattern
****
***
**
*
     # if boolean is False and n number of rows.
'''

n = int(input("Enter a number of rows : "))
inp = int(input("Enter 1 or 0 : "))
booltype = bool(inp)
if booltype == True:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end='')
        print()

elif booltype == False:
    for x in range(n, 0, -1):
        for y in range(1, x + 1):
            print("*", end=" ")
        print()





