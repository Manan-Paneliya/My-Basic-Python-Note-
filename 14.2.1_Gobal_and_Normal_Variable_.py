a = 10  # Global


def vikas():
    # a = 15  # Normal
    b = 35  # Normal

    # we cannot change global variable inside the function
    # if we want to change global variable inside the function , we required to use global Keyword
    global a
    a = a

    print(a, b)  # inside function it take first normal, after check global, then if it not find , then occures error.


vikas()

# global keyword

a1 = 10


def bheem():
    # a1 = a1 + 10   # it does not work , because it requires to use global variable before it .
    global a1
    a1 = a1 + 10
    print(a)
