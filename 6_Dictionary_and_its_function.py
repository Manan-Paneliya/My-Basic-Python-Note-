### Dictionary
"""
It is Odered after "python 3.7 vesion "
It is Changeable
It Does not Allow Duplicate
"""


d1 = {}          # it is Blank dictionary
print(type(d1))  # it returns which type of d1 is
d2 = {'manan':33                                    # manan is key and 33 is item or value
      ,'naman':56
      ,'raman':78
      ,'aman': {'sci':98,'math':67,"eng":89}  }     # nested dictionary
print(d2)
print(d2["raman"])   # it returns the value of raman
print(d2["aman"]['math'])
print("\n********************************** 1 *********************************\n")

# add any key and value in dictionary
d2['khaman'] = 99
print(d2)
print("\n********************************** 2 *********************************\n")

## Delete and copy
del d2['khaman']      # it delete 'khaman' from Dictionary
print(d2)
d3 = d2.copy()        # it copy the values of Dictionary from d2 to d3
print(d3)
print("\n********************************** 3 *********************************''\n'")

# get value of any key from dictionary
print(d2.get("raman"))    # it gives a value of 'reman' from divtionary
print(d2)
print("\n********************************** 4 *********************************\n")

# update Dictionary
d2.update({'khaman': 100})    # it can update and add 'khaman' to Dictionary
print(d2)
print("\n********************************** 5 *********************************\n")

# keys and items
print(d2.keys())   # it print only keys of Dictionary
print(d2.items())  # it print key-value pair of Dictionary

print("\n********************************** 6 *********************************\n")

#### Dictionary notes updated version ####
print("\n******************* Dictionary notes updated version ******************\n")

dict1 = {
      "name":"manan",
      "roll no":"16",
      "sub":"python"
}
## Access Value of specific key
print(dict1["name"])
print("\n********************************** 7 *********************************\n")

## It can be List as a value of dictionary
#for Example
dict2 = {"list":[1,2,3,4,5]}
print(dict2)
print(dict2["list"])

print("\n********************************** 8 *********************************\n")

## Accessing Value of given key in another way
print(dict1.get("sub"))

print("\n********************************** 9 *********************************\n")

## get all Keys
print(dict1.keys())

print("\n********************************** 10 *********************************\n")

## get all values
print(dict1.values())

print("\n********************************** 11 *********************************\n")

## Return all Items of dictionary
print(dict1.items())

print("\n********************************** 12 *********************************\n")

## Adding a Value or Change a value (Both have same mathod )
# change a value
print(dict1)
dict1["name"] = "hari"
print(dict1)
# add a Value
dict1["roll no"] = "36"
print(dict1)

print("\n********************************** 13 *********************************\n")

## Update Method (It is same previous change method )
dict1.update({"name":"xyz"})
print(dict1)

print("\n********************************** 14 *********************************\n")

## Removing Item of Dictionary
# pop method   (It remove a given item)
dict1.pop("name")
print(dict1)

# popitem method   (It removes a last item)
dict1.popitem()
print(dict1)

print("\n********************************** 15 *********************************\n")

### print Dictionary thorough a loop###
dict2 = {"name":"manan","roll no":"12","collage":"GP,Rajkot","div":"B2","branch":"IT engineering"}

# print all keys , one by one
for x in dict2:
      print(x)
print("\n********************************** 16 *********************************\n")
# print all values , one by one .
for x in dict2:
      print(dict2[x])
print("\n********************************** 17 *********************************\n")
# return all Values
for x in dict2.values():
      print(x)
print("\n********************************** 18 *********************************\n")
#it returns all items , one by one .
for x in dict2.items():
      print(x)
print("\n********************************** 19 *********************************\n")
### Copy a Dictionary
dict3 = dict2.copy()


