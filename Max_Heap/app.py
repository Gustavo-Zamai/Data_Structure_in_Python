'''
- Similiar to stack and queue
- Every node <= its parent, parent must have been greater than his childrens, right or left.
- Complete Binary Tree 
- Highest number always will be on top of the heap
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- Insert in O (log n)
- Get Max in O (1)
- Remove Max in O (log n)

- Easy to implement using List
- access parent: returning the index 
    index i = 4
    parent(i) = i / 2 = 2
    left(i) = i * 2 = 8
    right(i) = (i * 2) + 1 = 9

Operations:
    - Push (insert):
        - add value to end of array, 
        - float it up its proper position, 
        - comparing to his current parent value
    - Pop (remove max):
        - Move max to end of array
        - Delete it
        - Bubble down the item at 1 index to its proper position
        - Return max
    - Peek (get max) - return the value at heap[1], top of the heap

Functions:
    - Public:
        - push, pop, peek
    - Private:
        - swap, __floatUp__, __bubbleDown__, __str
'''
class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) -1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            max_value = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max_value = self.heap.pop()
        else:
            max_value = False
        return max_value
    
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent_index = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent_index]:
            self.__swap(index, parent_index)
            self.__floatUp(parent_index)

    def __bubbleDown(self, index):
        left_child_index = index * 2
        right_child_index = (index * 2) + 1
        largest_index = index
        if len(self.heap) > left_child_index and self.heap[largest_index] < self.heap[left_child_index]:
            largest_index = left_child_index
        if len(self.heap) > right_child_index and self.heap[largest_index] < self.heap[right_child_index]:
            largest_index = right_child_index
        if largest_index != index:
            self.__swap(index, largest_index)
            self.__bubbleDown(largest_index)

    def __str__(self):
        return str(self.heap)
    
# Testing maxheap functions
heap = MaxHeap([95, 3, 21])
print('Initial heap:', heap)
heap.push(10)
print('Heap after pushing:', heap)
print('Peek:', heap.peek())
print('Popped item:', heap.pop())
print('Heap after popping:', heap)
print('Peek:', heap.peek())