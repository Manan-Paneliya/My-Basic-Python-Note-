##open using normal method
# f = open("28.1_txt1.txt", "rt")
# rd = f.read()
# print(rd)

#####   OR   #####

## open using with block

with open("28.1_txt1.txt", "a") as f:
    rd = f.write("\nJay Swaminarayan")
    print(rd)
