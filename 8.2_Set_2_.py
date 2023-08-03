# another Functions of Set

# union : it makes third set , and add addition of 2 set .
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)

# intersection_update()
set4 = {"apple" , "banana" ,"cherry"}
set5 = {"google","Microsoft","apple"}
set4.intersection_update(set5)
print(set4)

#  intersect()
set4.intersection(set5)            # for we get duiplicate as a set
print(set4)

#  symmetric_difference_update()
set4.symmetric_difference_update(set5)  # keep all axcept duiplicate of set4
print(set4)

print("***************** Updeted version of set ******************* ")
s1 = {1,2,3,4,5}                       # [
s2 = {6,7,8,9}                         # |        it
# --> Join 2 set                       # |     excludes
s3 = s1.union(s2)                      # |     duplicate
s1.union(s2)   # make union at s1      # [       value
# --> intersection_update()
s1.intersection_update(s2)     # only return duplicate in s1

# --> intersaction()
s4 = s1.intersection(s2)       # it also return duplicate value but in new variable

# --> symmetric_difference_update()
s1.symmetric_difference_update(s2)  # Keep all , but not the Duplicate (in same variable)

# --> symmetric_difference()
# s5 = s1.symmetric_difference()  # it returns all EXCEPT duplicate