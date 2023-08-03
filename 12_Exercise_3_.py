# Practical 4
''' Write a programm to geuss the Number :
                                           in which you select any number ,
                                           and take input number from user ,
                                           if user's input is less than your selected number, again take input and
                                           print "input more" and if user's input is more than your selected
                                           number, again take   input and print "input less" and so no .
                                           Give 9 chance to input .
                                           if user input your selected number ,print "You Win" ,
                                           otherwise print "you lose".'''
mynum = 5

gus = 1
print("you have 9 chance to gauss\n")
inp =  int(input("gausses the number : "))
while gus < 9 :
    if inp > mynum:
        print("you required to take less value","\n""you have ",9 - gus,"chance left")
        print()
        inp = int(input("\ninput again : "))
    elif inp < mynum:
        print("you required to take more value","\n""you have ",9 - gus,"chance left")
        inp = int(input("\ninput again : "))
    else :
        print("you are WIN in ",gus , "chances")
        break
    gus = gus + 1

if gus > 9 :
    print("you are DEFEAT")