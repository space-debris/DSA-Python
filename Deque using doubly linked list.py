class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
    
class Deque:
    def __init__(self):
        self.front=None #variables
        self.rear=None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count==0
    
    def insert_front(self,data):
        nn=Node(data,None,self.front)
        if self.is_empty():
            self.rear=nn
        else:
            self.front.prev=nn
        self.front = nn
        self.item_count +=1
    
    def insert_rear(self,data):
        nn=Node(data,self.rear)
        if self.is_empty():
            self.front=nn
        else:
            self.rear.next=nn
        self.rear=nn
        self.item_count +=1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count -=1
        
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
        self.item_count -=1
        
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count
        
d = Deque()
d.insert_front(10)
d.insert_front(20)
d.insert_rear(30)
d.insert_rear(40)
print("rear is ", d.get_rear()," front is ",d.get_front())