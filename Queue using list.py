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
        if not self.is_empty():
            self.mylist.remove(self.mylist[0])
        else:
            raise IndexError("queue underflow")

    def get_front(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("queue underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("queue underflow")
    
    def size(self):
        return len(self.mylist)

q = Queue()

try:
    print(q.get_front())
except IndexError as ie:
    print(ie.args[0])
    
q.is_empty()
q.enqueue(5)
q.dequeue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
print(q.mylist)
print(q.get_rear())
print(q.size())