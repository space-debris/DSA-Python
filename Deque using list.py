class Deque:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        self.items.insert(0,data)
    
    def insert_rear(self,data):
        self.items.append(data)
    
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("deque is empty")
    
    def delte_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("deque is empty")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("deque is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("deque is empty")
    
    def size(self):
        if not self.is_empty():
            return len(self.items)
        else:
            raise IndexError("deque is empty")
            