'''
 - Immutable - cant change or add items
 - Useful for fixed data
 - Faster than list - for finding items
 - Sequence type - all the above function will work with tuples
'''
# Constructors - create a new tuple
x = ()
x = (1, 2, 3)
x = 1, 2, 3
x = 2, # the comma tells python it's a tuple and not a int
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1) # change list to tuple
print(x, type(x))

# tuples are immutable, but member objects may be mutable
x = (1, 2, 3)
# del(x[1])  fails
# x[1] = 8   fails
print(x) # output = (1, 2, 3)

y = ([1, 2], 3) # first item is a list
del(y[0][1])  # delete the 2
print(y) # output = ([1], 3)

# Concatenating two tuples works
y += (4, ) 
print(y) # output = ([1], 3, 4)