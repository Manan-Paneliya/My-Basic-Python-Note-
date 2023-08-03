#### File Handling ####

## It Only read a given file .
f = open("24.1_TextFile.txt", "r")
rt = f.read()
print(rt)
f.close()
print("************************** 1 **************************")

## read only a single line
f2 = open("24.1_TextFile.txt", "r")
rt2 = f2.readline()
print(rt2)
f2.close()
print("************************** 1 **************************")
## read all lines in a list form

f2 = open("24.1_TextFile.txt", "r")
rt2 = f2.readlines()
print(rt2)
f2.close()