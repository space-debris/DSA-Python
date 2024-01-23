class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
class CLL:
    def __init__(self,last=None):
        self.last = last
    def is_empty(self):
        if self.last == None:
            return True
    def insertatstart(self,data):
        nn = Node(data)
        if self.is_empty():
            nn.next=nn
            self.last = nn
        else:
            nn.next = self.last.next
            self.last.next=nn
    def insertatlast(self,data):
        nn = Node(data)
        if self.is_empty():
            nn.next=nn
            self.last = nn
        else:
            nn.next = self.last.next
            self.last.next = nn
            self.last = nn
        