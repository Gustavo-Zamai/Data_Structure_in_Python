# Sortable

# Constructors - creating a new list
x = list() # create a empty list
y = ['a', 25, 'dog', 8.43] # add the items we want in the list directly 
tuple1 = (10, 20)
z = list(tuple1) # transform a tuple into a list

# list comprehension
a = [m for m in range(8)]
print(a) # output = [0,1,2,3,4,5,6,7]
b = [i**2 for i in range(10) if i>4]
print(b) # output = [25, 36, 49, 64, 81] 5**2, 6**2, 7**2, 8**2, 9**2

# Delete - delete a list or an item in a list
x = [5, 3, 8, 6]
del(x[1]) # delete 3
print(x) # output = [5, 8, 6]
del(x) # delete the list x

# Append - append an item to a list
x = [5, 3, 8, 6]
x.append(7) # add 10 to the end of the list
print(x) # output = [5, 3, 8, 6, 7]

# Extend - append a sequence to a list
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y) # add the elements of y to the end of x
print(x) # output = [5, 3, 8, 6, 12, 13]

# Video was at 19:49