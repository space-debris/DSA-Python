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
        return self.front==None
    
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
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -=1
    
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("No data in the queue")
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.rear.item
            
        
    def size(self):
        return self.item_count
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.get_front())
print(q.get_rear())

    
            
            