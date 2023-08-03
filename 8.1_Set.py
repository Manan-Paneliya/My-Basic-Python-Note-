# # *** set in Python ***  : set is immutable (means that its element cannot change)
# """
# # it is unodered
# # it is Unchangable
# # it does not allow Duplicate
# """

# set0 = {1, 2, 3, 4}  # set is write like this  , its element cannot repeat
# set2 = {1, 2, 2, 3}  # also write like this
# set1 = set()  # this is empty set

# # construction of Set
# print(set0)
# print(set0)
# print(type(set1))
# print(type(set2))
# print(set2)
# print("'\n'********************************** 1 *********************************''\n'")

# # add function

# set0.add(5)
# set0.add(5)  # it cannot add 5 second time
# print(set0)
# print("'\n'********************************** 0.13 *********************************''\n'")

# # union function
# set3 = set0.union({6, 7, 8})  # it take value from set0 and add to {6, 7, 8} ,
# # and it is important to assign variable, like set3
# print(set0, set3)
# print("'\n'********************************** 3 *********************************''\n'")

# # intersection Function
# set4 = {9, 2, 3}
# print(set4.intersection({4, 9, 3, 6}))  # it means that print matching element in set4 and {4, 9,3, 6}
# print()
# print("'\n'********************************** 4 *********************************''\n'")

# # disjoint function
# s = {1, 2, 3}
# s1 = {4, 5, 6}
# s2 = {4, 5, 6, 1}
# print(s.isdisjoint(s1))  # it is true if s and s1 has different elements and no one element is common .
# print(s.isdisjoint(s2))  # it is false if any element are common in s and s2 .
# print("'\n'********************************** 5 *********************************''\n'")

# # remove fumction
# ss = {1, 2, 3}
# ss.remove(3)  # it removes 3 in ss
# print(ss)
# print("'\n'********************************** 6 *********************************''\n'")

# # Other Function
# set5 = {0.5, 1, 2, 3, 4, 5, 6}
# print(len(set5))
# print(max(set5))
# print(min(set5))
# print(type(set5))

# print("'\n'******************** Updated Notes of Set ******************''\n'")
# print("Updated Notes of Set")
# # python Set
# myset = {"apple", "banana", "cherry"}

# print("'\n'********************************** 01 *********************************''\n'")
# # Find lenth fo set
# print(len(myset))

# print("'\n'********************************** 02 *********************************''\n'")
# # Set() Construction
# myset = {"apple", "banana", "cherry"}

# print("'\n'********************************** 03 *********************************''\n'")
# # Access item of set
# for x in myset:
#     print(x)

# print("'\n'********************************** 04 *********************************''\n'")
# # check a perticular item are present in set or not
# print("banana" in myset)  # it returns True ,if "banana" is present in myset, otherwise returns false

# print("'\n'********************************** 05 *********************************''\n'")
# # add item in set using add() method
# myset.add("mango")
# print(myset)

# print("'\n'********************************** 06 *********************************''\n'")
# # add set ot another set ,using update() mathod
# myset2 = {"grapes", "watermalon"}
# myset.update(myset2)
# print(myset)

# print("'\n'********************************** 07 *********************************''\n'")
# # add any variable to set
# # for example we can also add any list, tuple,...etc as a element of set .
# mylist = ["kiwi", "orange"]
# myset.update(mylist)
# print(myset)
# print("'\n'********************************** 08 *********************************''\n'")

# # remove an item of set sre remove() mathod and discard() mathod .
# myset.remove("banana")
# print(myset)

# print("'\n'********************************** 09 *********************************''\n'")
# ''' remove() and discard() method has work as same function 
#  a single difference is that : if we use remove() and we remove a element which is not present in set it occuers error 
#                               : in case we use discard() for remove it will not occurs error . '''
# myset.discard("chikoo")  # "chikoo" are not present in myset yet it will not occur ERROR
# print(myset)

# print("'\n'********************************** 0.10 *********************************''\n'")
# ''' ### pop method ###
#  you can also use th pop() method to remove an item but this method will remove th elast item , 
#  remember  that set are unodered so you will not know what item get remove .'''

# print("'\n'********************************** 0.11 ********************************''\n'")
# myset3 = {"apple", "banana", "cherry"}
# myset3.pop()
# print(myset3)

# print("'\n'********************************** 0.12 ********************************''\n'")
# # clear()
# # it will empty the set
# myset4 = {"apple", "banana", "cherry"}
# myset4.clear()
# print(myset4)

# print("'\n'********************************** 0.13 *********************************''\n'")
# # del function
# # the del function delete set completely
# myset5 = {"apple", "banana", "cherry"}
# del myset5
# # we can not print myset5 because it is totally deleted, myset5 is not exist .

# print("'\n'********************************** 0.13 *********************************''\n'")

# """
# s1.add(item name)   -- add item
# s1.update(s2)       -- add item or another set
# s1.remove(item)     -- if we use remove() and we remove a element which is not present in set it occuers error 
# s1.dicard(item)     --  in case we use discard() for remove it will not occurs error .
# s1.pop()            -- in this case it removes last item
# print(s1)
# s1.clear()  
# del s1
# """
s = (1,2,3)
s1 = (4,5)
s2 = s + s1
print(s2)