class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self.items)
    
      
    
    