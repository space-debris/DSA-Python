class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class Stack:
    def __init__(self):
        self.top=None
        self.item_count=0
    def is_empty(self):
        return self.top == None
    def push(self,data):
        nn = Node(data,self.top)
        self.top=nn
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            data = self.top.item
            self.top=self.top.next
            self.item_count -=1
            return data
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise self.is_empty()
    def size(self):
        return self.item_count

s= Stack()
s.push(10)
s.push(20)
s.push(30)
print("total elements iin the stack",s.size())
print("top element in the stack is ", s.peek())
print("poped element is",s.pop())
print("total elements iin the stack",s.size())
print("top element in the stack is ", s.peek())