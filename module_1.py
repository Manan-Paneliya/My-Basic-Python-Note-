def sum(x, y):
    return x + y


def mul(x, y):
    return x * y


# if we use any file to another file using import, then __name__ of this imported is not equal to "__main__".
#  otherwise we run any py file (not import from any )  __name__  of this file is __main__.
if __name__ == '__main__':
    print("Jay Swaminarayan")
    print(sum(2, 2))
    print(mul(5, 5))
