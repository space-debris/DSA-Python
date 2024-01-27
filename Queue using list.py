class Queue:
    def __init__(self):
        self.mylist = [] 
        # empty list object as instance object member of the queue
        self.front=None
        self.rear=None
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        self.mylist.append(data)
    
    def dequeue(self):
        self.mylist.remove(self.mylist[0])
    
    def get_front(self):
        return self.mylist[-1]
    
    def get_rear(self):
        return self.mylist[0]
    
    def size(self):
        return len(self.mylist)

