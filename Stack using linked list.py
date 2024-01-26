class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class Stack:
    def __init__(self):
        self.top=None
        self.item_count=None
    def is_empty(self):
        return self.top == None
    def push(self,data):
        nn = Node(data,self.top)
        self.top=nn
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start=self.start.next
            self.item.count -=1
            return data
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item