class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class DLL:
    def __init__(self,start = None):
        self.start = start
        
    def isempty(self):
        return self.start==None
    
    def insertatstart(self,data):
        n = Node(None,data,self.start)
        if not self.isempty():
            self.start.prev = n
        self.start = n
        
    def insertatlast(self,data):
        temp = self.start
        if self.start != None:
            while (temp.next != None):
                temp=temp.next
            nn = Node(temp,data,None)
        if temp == None:
            self.start = nn
        else:
            temp.next = nn
            
    def search(self,data):
        temp = self.start
        while temp != None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insertafter(self,temp,data):
        if temp is not None:
            nn = Node(temp,data,temp.next)
            if temp.next is not None:
                nn.next= temp.next.prev
            temp.next = nn
        
    def printall(self):
        temp = self.start
        if temp is not None:
            while temp is not None:
                print(temp.item)
                temp = temp.mext
     