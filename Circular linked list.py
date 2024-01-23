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
    def search(self,data):
        if self.is_empty:
            return None
        temp=self.last.next
        while temp != self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item == data:
            return temp
        return None
    def insertafter(self,temp,data):
        if temp is not None:
            nn = Node(data,temp.next)
            temp.next = nn
            if temp==self.last:
                self.last=nn
    def printlist(self):
        if not self.is_empty():
            temp=self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp=temp.next
            print(temp.item,end="/n")
    def deletefirst(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last=None
            else:
                self.last.next=self.last.next.next
    def deletelast(self):
        if  not self.is_empty():
            if self.last == self.last.next:
                self.last=None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    def deleteitem(self,data):
        if not self.is_empty():
            if self.last == self.last.next:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.deletefirst()
                else:
                    temp = self.last.next
                    while temp != self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.deletelast()
                            break
                        if temp.next.item == data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
                    
            
        
            
        