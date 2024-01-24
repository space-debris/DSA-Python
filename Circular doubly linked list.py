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
            self.start=nn
        else:
            nn.next=self.start
            nn.prev=self.start.prev
            self.start.prev.next=nn
            self.start.prev=nn
    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp != self.start:
            if temp.item==data:
                return temp
            temp=temp.next
    def searchtest(self,data):
        temp=self.start
        if temp==None:
            return None
        while temp.next != self.start:
            if temp.item==data:
                return temp
            temp=temp.next
    def insertafter(self,temp,data):
        if temp is not None:
            nn=Node(temp,data,temp.next)
            temp.next=nn
            temp.next.prev=nn
    def printcdll(self):
        if not self.isempty():
            temp=self.start
            while temp.next is not self.start:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item,end="\n")
    def deletefirst(self):
        if not self.isempty():
            if self.start.prev==self.start.next:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    def deletelast(self):
        if not self.isempty():
            if self.start.prev==self.start.next:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def deleteitem(self,data):
        if not self.isempty():
            if self.start.item==data:
                self.deletefirst()
            else:
                temp=self.start.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                        break
                    temp=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.count = 0
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count ==1:
            raise StopIteration
        else:
            self.count = 1 #first iteration ko cross kr dia hai 
        data=self.current.item
        self.current=self.current.next
        return data
    
mylist=CDLL()
mylist.insertatstart(10)
mylist.insertatlast(20)
mylist.insertatlast(30)
mylist.insertatlast(40)
mylist.insertafter(mylist.search(30),34)
mylist.insertafter(mylist.searchtest(34),38)
mylist.printcdll()

for x in mylist:
    print(x,end=" ")
        
                    
                
        
                
            

        
            