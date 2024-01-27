class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self,data):
        nn=Node(data)
        if self.is_empty():
            self.front=nn
        else:
            self.rear.next=nn
        self.rear=nn
        self.item_count +=1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.rear == self.front:
            self.rear = self.rear = None
        else:
            self.rear = self.rear.next
        self.item_count -=1
    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("No data in the queue")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("No data in the queue")
        
    def size(self):
        return self.item_count
    
q = Queue()

    
            
            