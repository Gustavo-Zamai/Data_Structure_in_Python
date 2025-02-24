'''
 - Store non-duplicate items
 - Very fast access vs Lists - large items
 - Math Set ops (union, intersect)
 - Sets are Unordered - cant sort a set
'''
# Constructors - create new sets
x = {3, 5, 3, 5}
print(x) # output = {3, 5}

y = set()
print(y) # output = set()

list1 = [2, 3, 4]
z = set(list1) # convert list to set
print(z) # output = {2, 3, 4}

# Set operations
x = {3, 8, 5}
print(x) # output = {3, 8, 5}
x.add(7) # add the item 7 
print(x) # output = {3, 8, 5, 7}

x.remove(3) 
print(x) # output = {8, 5, 7}

# get length of set
print(len(x)) # output = 3

# check if item exists in set
print(5 in x) # output = True

# pop random item from set
print(x.pop(), x) # output = 8 , {5, 7}

# delete all items from set
x.clear()
print(x) # output = set()

'''
Mathematical set operations:
- Union: s1 | s2 (OR)
- Intersection: s1 & s2 (AND)
- Symmetric Difference(in s1 but not in s2) s1 ^ s2 (XOR)
- Difference(in s1 but not in s2) s1 - s2
- Subset (s2 contains s1) = s1 <= s2
- Superset (s1 contains s2) = s1 >= s2
'''

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 & s2) # output = {3}
print(s1 | s2) # output = {1, 2, 3, 4, 5}
print(s1 ^ s2) # output = {1, 2, 4, 5}
print(s1 - s2) # output = {1, 2}
print(s2 - s1) # output = {4, 5}
print(s1 <= s2) # output = True
print(s1 >= s2) # output = False