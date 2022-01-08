dict1 = {'apple':"Red","orange":"Orange",'banana':"Yellow","guava":'Green'}

# it is the pair of key values, every element first part before semicolon is the key whose value is the seconod part value

# these are not iterable like string and list

# if want to add an element
dict1["runs"] = 21
# another method is
dict1.update({"milk":"White"})
print(dict1)
# if we want to delete an element
del dict1["runs"]
print(dict1)
# if u want to make a copy of it
dict2 = dict1.copy()
print(dict2)
# if we want to see the key present in that dict
print(dict1.keys())




