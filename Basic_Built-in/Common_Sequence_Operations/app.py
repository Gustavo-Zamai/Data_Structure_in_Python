# indexing, start in 0 [0]
# String
x = 'frog'
print(x[3]) # output = g

# list
y = ['pig', 'cow', 'horse']
print(y[1]) # output = cow

# tuple
z = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(z[0]) # output = Kevin

# Slicing [start : end+1 : step]
a = 'computer'
print(a[1:4])
print(a[1:6:2])
print(a[-1])
print(a[::-1])

# Adding and concatenating, use + to combine
# String
q = 'horse' + 'shoe'
print(q) # output = horseshoe

# list
w = ['pig', 'cow'] + ['horse']
print(w) # output =  ['pig', 'cow', 'horse']

# tuple
e = ('Kevin', 'Nikolas', 'Jenny') + ('Craig',)
print(e) # output = ('Kevin', 'Nikolas', 'Jenny', 'Craig')

# Multiplying
# String
d = 'bug' * 3
print(d) # output = bugbugbug

# list
r = [8, 5] * 3
print(r) # output = [8, 5, 8, 5, 8, 5]

# tuple
f = (2, 4) * 3
print(f) # output = (2, 4, 2, 4, 2, 4)

# Checking membership - verifica se o elemento está ou não na sequencia (in ou not int)
# String
b = 'bug'
print('u' in b) # output = True

# list
v = ['pig', 'cow', 'horse']
print('cow' not in v) # output = False

# tuple
h = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print('Nikolas' in h) # output = True

# Iterating (for)
# item
m = [7, 8, 3]
for item in m:
    print(item) # output = 7 \n 8 \n 3

# index & item
n = [7, 8, 3]
for index, item in enumerate(n):
    print(index, item) # output = 0 7 \n 1 8 \n 2 3

# number of items - count items in a sequence
# String
l = 'bug'
print(len(l)) # output = 3

# list
t = ['pig', 'cow', 'horse']
print(len(t)) # output = 3

# tuple
k = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(len(k)) # output = 4

# Minimum - find minimum item in a sequence
# String
o = 'bug'
print(min(o)) # output = b

# list
p = ['pig', 'cow', 'horse']
print(min(p)) # output = cow

# tuple
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(min(u)) # output = Craig

# Maximum - find maximum item in a sequence
# String
o = 'bug'
print(max(o)) # output = u

# list
p = ['pig', 'cow', 'horse']
print(max(p)) # output = pig

# tuple
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(max(u)) # output = Nikolas

# Sum - find the result of a sum of items in a sequence
# String -> Error

# list
y = [2, 5, 8, 12]
print(sum(y)) # output = 27
print(sum(y[-2:])) # output = 20

# tuple
z = (50, 4, 7, 19)
print(sum(z)) # output = 80

# Sorting - return a sort list of items in a sequence
# String
o = 'bug'
print(sorted(o)) # output = b, g, u

# list
p = ['pig', 'cow', 'horse']
print(sorted(p)) # output = cow, horse, pig

# tuple
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(sorted(u)) # output = Craig, Jenny, Kevin, Nikolas

# Sorting by secondd letter
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(sorted(u, key=lambda i: i[1])) # output = Kevin, Jenny, Nikolas, Craig

# Count(item) - returns count of a item
# String
x = 'hippo'
print(x.count('p')) # output = 2

# list
p = ['pig', 'cow', 'horse', 'cow']
print(p.count('cow')) # output = 2

# tuple
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(u.count('Kevin')) # output = 1

# Index(item) - return the index of a item, or the first item
# String
x = 'hippo'
print(x.index('p')) # output = 2

# list
p = ['pig', 'cow', 'horse', 'cow']
print(p.index('cow')) # output = 1

# tuple
u = ('Kevin', 'Nikolas', 'Jenny', 'Craig')
print(u.index('Kevin')) # output = 0

# Unpacking - unpack the n items into a variables
p = ['pig', 'cow', 'horse']
a, b, c = p
print(a, b, c) # output = pig, cow, horse









