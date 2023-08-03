### Make a Foulty Calculator ###
''' input 2 numbers from a user ,and choose operator(+,-,*,/) by user
  exept some expression are permanent , this are - 45 * 3 = 555
                                                 - 56 + 9 = 77
                                                 - 56 / 6 = 4  '''

print('d for Division \nm for Multiplication \na for Addition \ns for Substration')
choose = input('enter any(d,m,a,s) : ')
choose.lower()
n1 = int(input('enter a First number : '))
n2 = int(input('enter a Second number : '))

if choose == 'd':
        if n1 == 56 and n2 == 6 :
            print('Division is 4')
        else:
            print('Division is ',n1/n2)
elif choose == 'm':
    if n1 == 45 and n2 == 3:
        print('Multiplication is 555')
    else:
        print('Multiplication is ',n1*n2)
elif choose == 'a':
    if n1 == 56 and n2 == 9:
        print('addition is 77')
    else:
        print('Addition is ',n1 + n2)
elif choose == 's':
    print('Division is ',n1-n2)
else :
    print('envalid')


