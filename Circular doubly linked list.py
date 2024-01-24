class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start
    def isempty(self):
        if self.start==None:
            return True
    def insertatstart(self,data):
        nn=Node(None,data,None)
        if self.isempty():
            nn.prev=nn
            nn.next=nn
        else:
            nn.next=self.start
            nn.prev=self.start.prev
            self.start.prev.next=nn
            self.start.prev=nn
        self.start=nn
    def insertatlast(self,data):
        nn=Node(None,data,None)
        if self.isempty():
            nn.prev=nn
            nn.next=nn
        else:
            nn.prev=self.start.prev
            self.start.prev.next=nn
            nn.next=self.start
            self.start.prev=nn
        
            