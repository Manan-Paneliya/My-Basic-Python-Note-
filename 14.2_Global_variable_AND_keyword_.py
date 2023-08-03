# Global Variable and global keyword
# Example
i = 23  # Global Variable



def prnt():
    global i  # it allows to change global variable inside the function , otherwise not
    i = i + 2
    m = 5  # Local Variable
    print(i, m)


prnt()


# global Variable : a variable which is define outside the function , and we can use inside the function.
# local Variable : a variable whih is define inside the function , we cannot use it outside the function.

## global keyword : using global keyword we can change global variable inside the function

# example of nested function
def vikas():
    x = 20

    def aakas():
        global x  # it does not work because it checks directly outside the whole function.
        # and it find outside the function.
        x = 88
        print(x)

    print(" before calling aakas()", x)
    print(" after calling aakas()", x)


vikas()
