from Singly_linked_list import *

class Queue(SLL):
    def __init__(self):
        super.__init__()
        self.item_count = 0
        # self.front = None
        # self.rear = None
    
    def is_empty(self):
        return super().is_empty()
    
    def enqueue(self,data):
        self.insert_at_start(data)
        
    def dequeue(self):
        self.delete_last()
        
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("queue is empty")
    
    def get_last(self):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError("queue is empty")
    