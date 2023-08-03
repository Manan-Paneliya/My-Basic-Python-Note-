set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))  # add 2 set and add to third set
print(set1|set2)

print(set1.intersection(set2))    # it print common element in 2 set
print(set1 & set2)

print(set1.difference(set2))  # it print unique element set1 which is not present in set2
print(set1 - set2)

s1 = {1,2,3}
s2 = {3,4,5}
print(s1.symmetric_difference(s2))  # it print only non duplicate value of s1 and s2

s3 = {1,2,3,4,5}
s4 = {6,7,8}
print(s3.isdisjoint(s4))   # it return true if both set are unique


s5 = {1,2,3,4,5,6}
s6 = {1,2,3,54}
print(s6.issubset(s5))

dict = {"Name":"Manan","roll":16,"class":"B2"}
print(dict[0])
print(dict.get())