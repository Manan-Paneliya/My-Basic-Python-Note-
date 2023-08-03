# Health managment System
# 3 person diet plan (harry,rohan,hammad)
# first of all we select who we want retrive (read diet plan) or lock
# if we selected lock and then we selected whose diet plan we want to write
# then you select (diet plan or exercise plan)
# similarly with retrieve also

# function is we use is provided ready mate
def getdate():
    import datetime
    return datetime.datetime.now()

inp = int(input("\nEnter who you want(retrieve(1) or lock(2)) : "))
if inp == 1:
    inpr = str(input("\nEnter whose diet you wants to see (harry(h), rohan(r),hammad(hm)) : "))
    inpr.lower()
    if inpr == "h":
        print("Click 'd' to show harry's diet plan\nClick 'e' to show harry's exercise plan")
        inprh = str(input("Enter : "))
        inprh.lower()
        if inprh == "d":
            a = open("18.2_harry_diet.txt","r")
            c1 = a.read()
            print(c1)

        elif inprh == "e":
            b = open("18.3_harry_exercise_.txt", "r")
            c2 = b.read()
            print(c2)
        else:
            exit()
    elif inpr == "r":
        print("Click 'd' to show rohan's diet plan\nClick 'e' to show rohan's exercise plan")
        inprr = str(input("Input : "))
        inprr.lower()
        if inprr == "d":
            c = open( "18.4_rohan_diet_.txt","r")
            c3 = c.read()
            print(c3)
        elif inprr == "e":
            d = open("18.5_rohan_exercise_.txt", "r")
            c4 = d.read()
            print(c4)
        else:
            exit()
    elif inpr == "hm":
        print("Click 'd' to show hammad's diet plan\nClick 'e' to show hammad's exercise plan")
        inprhm = str(input("Input : "))
        inprhm.lower()
        if inprhm == "d":
            e = open("18.6_hammad_diet_.txt","r")
            c5 = e.read()
            print(c5)
        elif inprhm == "e":
            f = open("18.7_hammad_exercise_.txt","r")
            c6 =f.read()
            print(c6)
        else:
            exit()
elif inp == 2 :
    inpl = str(input("\nEnter whose diet you wants to see (harry(h), rohan(r),hammad(hm)) : "))
    inpl.lower()
    if inpl == "h":
        print("Click 'd' to show harry's diet plan\nClick 'e to show harry's exercise plan")
        inplh = str(input("Enter : "))
        inplh.lower()
        if inplh == "d":
            harry_diet = input("Enter your Diet : ")
            with open("18.2_harry_diet.txt", "a") as a:
                a.write("["+str(getdate())+"]"+"\t"+":"+"\t"+harry_diet+"\n")

        elif inplh == "e":
            harry_exe = input("Enter your Exersice plan : ")
            with open("18.3_harry_exercise_.txt","a") as a:
                a.write("["+str(getdate())+"]"+"\t"+":"+"\t"+harry_exe+"\n")
            print("successfully Writen")
        else:
            exit()
    elif inpl == "r":
        print("Click 'd' to show rohan's diet plan\nClick 'e to show rohan's exercise plan")
        inplr = str(input("Enter : "))
        inplr.lower()
        if inplr == "d":
            rohan_diet = input("Enter rohan's diet plan : ")
            with open("18.4_rohan_diet_.txt","a") as a :
                a.write("["+str(getdate())+"]\t:\t"+rohan_diet+"\n")
            print("Sucessfully Writen")
        elif inplr == "e":
            rohan_exe = input("Enter rohan's exersice plan : ")
            with open("18.5_rohan_exercise_.txt","a") as a:
                a.write("["+str(getdate())+"]\t:\t"+rohan_exe+"\n")
            print("Sucessfully Writen")
        else:
            exit()
    elif  inpl == "hm":
        print("Click 'd' to show hammad's diet plan\nClick 'e to show hammad's exercise plan")
        inplhm = str(input("Enter : "))
        inplhm.lower()
        if inplhm == "d":
            hammd_diet = input("Enter hammad's diet plan : ")
            with open("18.6_hammad_diet_.txt","a") as a:
                a.write("["+str(getdate())+"]\t:\t"+hammd_diet+"\n")
            print("sucessfully Writen")
        elif  inplhm =="e":
            hammad_exe = input("Enter hammad's exersice plan : ")
            with open("18.7_hammad_exercise_.txt","a") as a:
                a.write("["+str(getdate())+"]\t:\t"+hammad_exe+"\n")
            print("Sucessfully Writen")
        else:
            exit()
    else:
        exit()