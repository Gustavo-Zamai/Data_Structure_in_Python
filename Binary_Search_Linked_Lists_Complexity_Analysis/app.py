# create a function to locate the number 7
def locate_card(cards, query):
    pass

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)
print(result)

# compare the result with output 3
result == output

# create dict a test to validate output
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

# outra maneira seria:
# locate_card(**test['input']) == test['output']
locate_card(test['input']['cards'], test['input']['query'] == test['output'])

""""
List possibles scenarios:
- number query occurs in the middle list cards
- query is the first element in cards
- query is the last element in cards
- cards contains just one element, which is query
- cards doesnt contain query
- cards is empty
- cards contains repeating numbers
- number query occurs more than one position in cards
"""

 # create test cases
tests = []

tests.append(test)

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards doesnt contain query, we will return -1 as output in this case
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can be repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query itself repeat, we pick the first element that satisfy the query
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)