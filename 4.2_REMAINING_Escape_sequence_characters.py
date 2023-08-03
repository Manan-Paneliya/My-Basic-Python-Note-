# Escape sequebnce characters
# // , \t , \n , \r .etc
# \t
a = ('\tJay Swaminarayan'.expandtabs(tabsize=10))  # we can define a size of tab
print(a)

print("123456789\rhell\rHari\rHari Krushna")    # it exclude a string befor "\r"

print("hello\bworld")
print("hello\b\bworld")
print("hello\b\b\bworld")
print("hello\b\b\b\bworld")
