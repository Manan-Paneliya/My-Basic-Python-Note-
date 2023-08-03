### String Operation ###

mystr = "Jay Swaminarayan"
# String indexing (means "J"=0,"a"=1,"y"=2," "=3,"S"=4,.........)
print(mystr[1])
print(mystr[3])
print(mystr[4])
print('********************************** 1 **********************************')

# String Slicing
print(mystr[4:9])# S=4 & i=8, it takes 1 less index number after ':'so we put +1 already 
print(mystr[4:16])
print(mystr[0:16])
print('********************************** 2 **********************************')

# Find length of String
print(len(mystr)) # it  gives 16 , but it is 15, we mind +1. 
print('********************************** 3 **********************************')

# Skiping of Characters
alpha = '123456789'
print(alpha[0:9:1])
print(alpha[0:9:2])   # it skip one character after a one character
print(alpha[0:9:3])   # it skip Two character after a one character
                      # and so on
print(alpha[::]) # [a,b,c] ,a = by default 0 , b = by default maximum length c = by defalt 1
print('********************************** 4 **********************************')

# inver indexing 
mystri = "Jay Swaminarayan."  #(means .=-1,n=-2,a=-3,y=-4,.........)
print(mystri[-2])
# invers slicing
print(mystri[-8:-1])
print('********************************** 5 **********************************')

### String Functions  ###
str1 = "My Loard Swaminarayan Hari Hari"
str2 = "hari"
print(str1.isalnum())          # it returns true if string cantain alphanumeric characters e.g - @Hari1837#$&
print(str2.isalpha())        # it returns true if string cantains only alphabets   e.g Hari   , space is not allow
print(str1.isalpha())
print(str1.endswith("yan"))  # it returns true, if "yan" is endswith str1
print(str1.count("H"))       # it count that how many "H" are present in str1
print(str1.count("Hari"))    # it count that how many "Hari" are present in str1
print(str2.capitalize())     # it capitalise our string FOR e.g   hari--->Hari
print(str1.find("L"))        # it find that "L" is present at which index of String

##### There are many string Function , Which is provide i internet #####

