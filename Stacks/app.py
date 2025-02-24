'''
LIFO: Last In First Out

- pop and push are from the TOP of stack
- Peek - get item on top of stack, without removing it
- Clear - remove all items from stack

Use Case:
 - Undo operation, can track which command have been executed
'''
# Stack using Python List
my_stack = list()

# push an item to the stack
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack) # output = [4, 7, 12, 19]

print(my_stack.pop()) # remove item 19, last in first out
print(my_stack.pop()) # remove item 12, the last item
print(my_stack) # output = [4,7]

'''
Stack using List with a Wrapper Class
'''

class Stack():
    def __init__(self):
        self.stack = list()
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    

my_stack = Stack() # instance Stack class
my_stack.push(1)
my_stack.push(3)
print(my_stack) # output = [1, 3]
print(my_stack.pop()) # remove item 3, otput = 3
print(my_stack.peek()) # show the items into Stack, output = 1
print(my_stack.pop()) # remove item 1, output 1
print(my_stack.pop()) # None, there's no item to remove

