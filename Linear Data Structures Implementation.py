# Linear Data Structures Implementation In Python
'''
[1] Stack
[2] Queue
[3] Linked list
[4] 
'''
class Stack:
    def __init__(self,items = [],duplicates = True):
        self.items = items
        self.duplicates = duplicates

    # Push function to add items to the end of the stack
    def push(self,item):
        self.items.append(item)
        return self.items
    
    # Pop function to remove item from the end of the stack    
    def pop(self):
        if len(self.items) > 0:
            item = self.items[-1]
            self.items.remove(item)
            print(f'{item} popped out of stack')
        else:
            print('Cannot pop from empty stack')
        return self.items
    
Ages = Stack([1,2],True)
print(Ages.push(3))
print(Ages.pop())

class Queue:
    def __init__(self, items = [], duplicates = True):
        self.items = items
        self.duplicates = duplicates
    
    # Returns True for Empty queue and False for non-empty queue
    def IsEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

    # Enqueue function add elements to the rear of the queue
    def enqueue(self,item):
        self.items.append(item)
        return self.items

    # Dequeue function removes elements from the front of the queue
    def dequeue(self):
        if self.IsEmpty() == False:
            n = self.items[0]
            self.items.remove(n)
        else:
            print('Cannot dequeue from an empty queue')
        return self.items

Graduates = Queue(['Joe','Nana','Kashby', 'Leroy', 'Page'],True)
print(Graduates.enqueue('Kojo'))
print(Graduates.enqueue('Fiifi'))
print(Graduates.dequeue())
            
class LinkedList:
    def __init__(self,items = [], pointers = []):
        self.items = items
        self.pointers = pointers

    # This generates the pointers
    def get_pointer():
        pass
    
    def insert(self,item,place):
        self.items.insert(0,item)
        self.pointers.insert(0,get_pointer(item))
    
    def remove(self,item,place):
        pass

    def find(self,item,place):
        pass
