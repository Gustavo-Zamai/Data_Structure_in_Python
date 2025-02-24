'''
- Key/Value pairs
- Hashmap/JSON = Dictionary in Python
- Dicts are Unordered - cant be sorted
'''
# Constructors - create a new dictionary
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(x) # output = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
print(x) # output = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x) # output = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}

# Dict operations
# add or update the value
x['shrimp'] = 38.2
print(x) # output = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7, 'shrimp': 38.2}

# delete an item
del(x['shrimp']) # pass the key
print(x) # output = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}

# get length of dict
print(len(x)) # output = 3

# delete all items
x.clear()
print(x) # output = {}

# delete the dict
del(x)

# Accessing keys and values in a dict
y = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(y.keys()) # output = dict_keys(['pork', 'beef', 'chicken'])
print(y.values()) # output = dict_values([25.3, 33.8, 22.7])
print(y.items()) # output = dict_items ([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])

# check if key exists in dict
print('pork' in y) # output = True
print('turkey' in y) # output = False

# check values exists in dict
print(25.3 in y.values()) # output = True
print(30 in y.values()) # output = False

# iterate over dict - random order
# Same result in this two for
for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)

