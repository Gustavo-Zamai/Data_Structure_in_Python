'''
Attr: 
   - Root: pointer to the beginning of the list
   - Size: number of nodes in the list

Operations:
    - find
    - add
    - remove
    print_list()
'''
# Node Class
class Node:

    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next_node = next
        self.previous_node = previous

    def __str__(self):
        return ('(' + str(self.data) + ')')

# Linked List Class, with methods
class LinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        current_node = self.root
        while current_node is not None:
            if current_node.data == data:
                return data
            else:
                current_node = current_node.next_node
        return None
    
    def remove(self, data):
        current_node = self.root
        previous_node = None

        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None: # data is in non-root
                    previous_node.next_node = current_node.next_node
                else: # data is in root node
                    self.root = current_node.next_node
                self.size -= 1
                return True # data removed
            else:
                previous_node = current_node
                current_node = current_node.next_node
        return False # data not found

    def print_list(self):

        current_node = self.root
        while current_node is not None:
            print(current_node, end='->')
            current_node = current_node.next_node
        print('None')

# Testing linked list
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list() # output: (12)->(8)->(5)->None

print('Size = ' + str(myList.size))
myList.remove(8)
print('Size = ' + str(myList.size))
print(myList.find(5))
print(myList.root)

'''
Circular Linked List

- Last pointer, points to first element of list, loopback
- Add: insert a new element at the second position, index 1
- Better for modeling continuos looping objects
'''
# Circular Linked List
class CircularLinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, data):
        current_node = self.root
        while True:
            if current_node.data == data:
                return data
            elif current_node.next_node == self.root:
                return False
            current_node = current_node.next_node

    def remove(self, data):
        current_node = self.root
        previous_node = None

        while True:
            if current_node.data == data: # found the item
                if previous_node is not None: # item is not in root
                    previous_node.next_node = current_node.next_node
                else: 
                    while current_node.next_node != self.root:
                        current_node = current_node.next_node
                    current_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True # item removed
            elif current_node.next_node == self.root:
                return False # item not found
            previous_node = current_node
            current_node = current_node.next_node

    def print_list(self):
        if self.root is None:
            return
        current_node = self.root
        print(current_node, end='->')
        while current_node.next_node != self.root:
            current_node = current_node.next_node
            print(current_node, end='->')
        print()

# Testing Circular Linked List
cll = CircularLinkedList()
for i in [5, 7, 3, 8, 9]:
    cll.add(i)

print("Size = " + str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
print(my_node, end='->')
for i in range(10):
    my_node = my_node.next_node
    print(my_node, end='->')
print()
        
cll.print_list()
cll.remove(8)
print(cll.remove(15))
print("Size = " + str(cll.size))
cll.remove(5)
cll.print_list()

'''
Doubly linked list

- Each node has both a next and previous pointer
'''
