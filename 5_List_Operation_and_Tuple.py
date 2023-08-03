### List and Tuple ###
'''List : is a mutable (means its element can be change) and write inside square braces-[]
   Tuple : is immutabe  (means its elements cannot be change) and write inside parentheses-()'''

### List : is a collection of elements or values

# LIst Indexing
menu = ['Dal', 'Bhat', 'Shak', 'roti', 'barphi', 'papad']
print(menu[3])  # it means 'roti'= 3.
print(menu[0])
print('********************************** 1 **********************************')

# Sorting a List  (sort and reverse)
list1 = [5, 9, 2, 4, 7, 3, 6, 1, 8]
list1.sort()  # it makes list become in a order
print(list1)
list1.reverse()
print(list1)
list1.reverse()
print('********************************** 2 **********************************')

# List Slicing
print(list1[:])  # Similar Rule of defalt in String Slicings
print(list1[0:5])
print(list1[::2])
print(list1[1:5:-2])  # in negative slicing ,we put starting and ending index , it gives blank List
print(list1[1:5:2])
print('********************************** 3 **********************************')

# len(),max() and min() Function
print(len(list1))  # it returns number of values are present in list1
print(max(list1))  # it returns maximum value of list
print(min(list1))  # it returns minimum value of list
print('********************************** 4 **********************************')

## append(),extend() and insert() Function
'''append : it is add a element in a list
   extend : it is add 2 list
   insert : it is add a element at a given index of list '''
# append()
list2 = []
list2.append(10)
list2.append(23)
list2.append(85)
print(list2)

# extend()
list3 = ['python', 'java', 'c', 'Ruby']
list3.extend(['HTML', 'css', 'javascript', 'php'])  # ['HTML','css','javascript'] is add to list3
print(list3)

# insert()
list3.insert(3, 'c++')  # "c++" is add in list3 at index 3
print(list3)
list3.insert(5, 'R')  # "R" is add in list3 at index 5
print(list3)
print('********************************** 5 **********************************')

# change a element of string at a perticular index
list3[9] = 'node js'
print(list3)
print('********************************** 6 **********************************')

### remove(),pop() and clear() Function
'''remove : it remove a element from list 
   pop : it remove element at a given index 
   clear " it remove all element of list'''

# remove()
list4 = ['dharm', 'bhakti', 'kam', 'gnan', 'veyrag', 'lobh', 'man', 'moh', 'irsiya']
list4.remove('irsiya')
print(list4)
list4.remove('moh')
print(list4)
"""print(list4.remove('irsiya'))"""  # it is not a right way to print , it returns none

# pop()
list4.pop()  # it romove last element of list
list4.pop()
print(list4)
list4.pop(2)
print("its my Gol : ", list4)

# clear()
enemy = ["kam", 'krodh', 'lobh', 'moh', 'ersia', 'matsar']
print('my enemy :', enemy)
enemy.clear()
print(enemy)
print('********************************** 7 **********************************')

## index(),count() and copy()
# index
list5 = ['lenovo', 'acer', 'dell', 'mac book', 'php', 'mac book', 'acer']
print(list5.index("php"))  # it returns index of 4 in list5
print(list5.index("mac book", 2))  # it returns index of second "mac book" in list5
print('********************************** 8 **********************************')

# count()
print(list5.count('acer'))  # it count a 'acer' are how many times present in list5

# copy()
cfam = ['tiger', 'lion', 'leapord']
print(cfam)
anml = cfam.copy()
anml.extend(['horse', 'elephant', 'monkey'])
print(anml)
print('********************************** 9 **********************************')

# list function
print(list([]))  # we can write list like this

# range function
print(list(range(10)))  # it print list of 1 to 9 numbers
print(list(range(1, 11)))  # it print list of 1 to 10 numbers
print(list(range(1, 11, 2)))  # it print list of 1 to 10 numbers with skip one element after one element print
print('********************************** 10 **********************************')

### Tuple

tup0 = (1)  # it returns 1   , (1) is not called tuple
tup01 = (1,)  # it returns (1,) , for 1 element in tuple we required to write a coma like this (1,)
tup1 = (1, 2, 3)  # it returns (1,2,3)
print(tup0)
print(tup01)
print(tup1)
print('********************************** 11 *********************************')

# Swap values of Variables
a = 3
b = 6
a, b = b, a
print(a, b)
####################################################
#     At last Search List Function and tuple function in Google for more learn      #
####################################################
a,b, c, d = (1,99,3,4)
print(b)
