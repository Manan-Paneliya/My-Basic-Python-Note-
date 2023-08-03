
me = "manan"
hoby = "object-oriented programming"


i = "Hello my name is %s , i am learning %s "%(me,hoby)
print(i)


# string formating
a = "Hello my name is {} , i am learning {} "
b = a.format(me, hoby)
print(b)

c = f"Hello my name is {me} , i am learning {hoby}"
print(c)