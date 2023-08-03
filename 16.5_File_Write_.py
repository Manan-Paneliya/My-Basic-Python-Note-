# write mode for file

'''
"w" : Write mode - if the file is exist , it makes a new file with our data.
                 - then allready the file is exist , it replace file data with our data,
"a" : append mode - we can add our data to another which is exst with their
"r+": read and write

'''
print('\n********************************** 1 *********************************\n')
# the below code : it makes a file (16.6_text_2_.txt) and add below data into it .
# "w" (Write mode)
f = open("16.6_text_2_.txt", "w")
f.write("Jay Swaminarayan My inspiration is gunatitanand Swami ")
f.close()

# in this case there are already exist a file(16.7_text_3_) and "a" (append mode) is add data to it .
f = open("16.7_text_3_.txt", "a")
f.write("\nJay Swminarayan welcome to Python")
f.close()

# Handle read and write both
f = open("16.8_text_4_.txt", "r+")  # in "r+" mode , if file is not exist it occures Error
print(f.read())
f.write("\nThank you Hari for giving me your saint and your happiness ")
