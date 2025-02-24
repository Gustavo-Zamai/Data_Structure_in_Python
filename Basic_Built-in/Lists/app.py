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

# Insert - insert an item at a specific index in a list, (index, item)
x = [5, 3, 8, 6]
x.insert(1, 7) # add item 7 to the 1 index position
print(x) # output = [5, 7, 3, 8, 6]
x.insert(1, ['a', 'm']) # add a list with 'a' and 'm', at the 1 index position
print(x) # output = [5, ['a', 'm'], 7, 3, 8, 6]

# Pop - remove the last item off the list
x = [5, 3, 8, 6]
x.pop() # remove the last item, 6,from the list
print(x) # output = [5, 3, 8]
print(x.pop()) # output = 8, the current last item

# Remove - remove the first occurrence of a specified item from the list
x = [5, 3, 8, 6, 3]
x.remove(3) # remove the first occurrence of 3, from the list
print(x) # output = [5, 8, 6, 3]

# Reverse - reverse the order of the list, changes the original list
x = [5, 3, 8, 6]
x.reverse() # reverse the order of the list
print(x) # output = [6, 8, 3, 5] 

# Sort - sort the list in ascending order, changes the original list
x = [5, 3, 8, 6]
x.sort() # sort the list in ascending order
print(x) # output = [3, 5, 6, 8]

# Reverse sort
x = [5, 3, 8, 6]
x.sort(reverse=True) # sort the list in descending order
print(x) # output = [8, 6, 5, 3]