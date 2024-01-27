class Queue(list):
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.remove(self[0])
        else:
            raise IndexError("queue underflow")

    def get_front(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("queue underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("queue underflow")
    
    def size(self):
        return len(self)

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
print(q)
print(q.get_rear())
print(q.size())