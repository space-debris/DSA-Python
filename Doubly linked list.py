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
            temp.next = nn
        else:
            print("list is empty")
            
    def search(self,data):
        if self.start != None:
            temp = self.start
            while data != temp.data:
                temp=temp.next
        else:
            print("not found")
     