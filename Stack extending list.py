class Stack(list):
    def isempty(self):
        return len(self)==0 #self is object of stack, hence object of list
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.isempty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.isempty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data): #restricting the use of list attributes
        raise AttributeError("no attribute named insert in stack")

s = Stack()
s.push(10)
print(s.peek())
        