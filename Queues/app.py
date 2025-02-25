'''
FIFO - First In First Out

- Enqueue - add an item in the end of the queue
- Dequeue - remove an item from the front of the queue

Use Cases:
- Filas da loterica
- Fila de atendimento bancario
- Atendimento médico

Deque is a double-ended queue
'''
# Queue using Python Deque
from collections import deque

my_queue = deque() # create an empty queue
my_queue.append(5) # add item 5
my_queue.append(10) # add item 10
print(my_queue) # output = [5, 10]
print(my_queue.popleft()) # remove item 5, first in first out

'''
Exercise:
- Write a wrapper class for the Queue class
- Trya adding enqueue, dequeue and get_size methods
'''
class Queue:
    def __init__(self):
        self.queue = deque() # create an empty queue
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None
    
    def get_size(self):
        return len(self.queue)
    
    def __str__(self):
        return str((self.queue))
    

my_queue = Queue() # instance Queue class
my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(6)
print(my_queue) # output = [1, 3, 6]
print(my_queue.dequeue()) # remove item 1, first in first out
print(my_queue.get_size()) # output = 2
print(my_queue) # output = [3, 6]