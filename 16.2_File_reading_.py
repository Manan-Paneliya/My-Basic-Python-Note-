print('\n********************************** 1 *********************************\n')
f = open("16.3_text.txt", "r")  # open the text file
content = f.read()  # read the text file
print(content)  # print the text file

f.close()  # it is required to close the file

print('\n********************************** 2 *********************************\n')
# it read only given number of words
f = open("16.3_text.txt", "r")
content = f.read(4)  # it means it read only 4 words of "16.3_text.txt"
print(content)

f.close()

print('\n********************************** 3 *********************************\n')
# it read next given number of words
f = open("16.3_text.txt", "r")
content = f.read(7)  # it means it read 7 words of "16.3_text.txt" and ignore above code of read 5 words
print(content)

f.close()

print('\n********************************** 4 *********************************\n')
f = open("16.3_text.txt", "r")
content = f.read()
print("Its my resume : ", content)  # it print a string before content read

f.close()

print('\n********************************** 5 *********************************\n')
f = open("16.3_text.txt", "r")
content = f.read(1234)  # it ignore extra content, and print only which is exist
print(content)

f.close()

# readline() function
print('\n********************************** 6 *********************************\n')
j = open("16.4_read.txt")
godname = j.readline()  # it read first line of 16.4_read.txt
print(godname)
godname = j.readline()  # it read second line of 16.4_read.txt
print(godname)
godname = j.readline()  # it read Third line of 16.4_read.txt
print(godname)

j.close()

# readlines() function : it read lines as a element under list
s = open("16.4_read.txt")
g2 = s.readlines()

### we can read and open any file , no matter it is text file , python file , c , java ,.......etc
