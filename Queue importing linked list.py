from Singly_linked_list import *

class Queue():
    def __init__(self):
        self.mylist = SLL()
        
    def is_empty(self):
        return self.mylist.is_empty()

    def enqueue(self,data):
        self.mylist.insert_at_start(data)
    
    def dequeue(self):
        self.mylist.delete_last()
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist.start.item
        else:
            raise IndexError("queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            temp =self.mylist.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("queue is empty")
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.get_front())
print(q.get_rear())