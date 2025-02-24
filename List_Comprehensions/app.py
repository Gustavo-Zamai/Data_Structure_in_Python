# basic format: new_list = [transform sequence [filter]]
# filter is optional
import random

# get values within range
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10)) # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# get square values
squares = [x**2 for x in under_10]
print('squares: ' + str(squares)) # output = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# get odd numbers using mod
odds = [x for x in under_10 if x % 2 != 0]
print('odds: ' + str(odds)) # output = [1, 3, 5, 7, 9]

# get multiples of 10
ten_x = [x * 10 for x in range(10)]
print('ten_x: ' + str(ten_x)) # output = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums)) # output = [2, 0, 7, 3]

# get a index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print('index = ' + str(idx[0])) # output = index = 2

# delete a item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)

