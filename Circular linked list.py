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
            print(temp.item,end="\n")
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
    def __iter__(self):
        if self.last == None:
            return CLLiterator(None)     
        else:
            return CLLiterator(self.last.next)           
            
class CLLiterator:
    def __init__(self,start):
        self.current=start #object banate hue pehle node ka ref supply krna padega 
        self.start=start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count==1: #wapas se pehle wale peagye yani, if ke baad vrna pehle hi stop
            raise StopIteration
        else:
            self.count=1
        data = self.current.item
        self.current = self.current.next
        return data
        
cll = CLL()
cll.insertatstart(10)
cll.insertatstart(20)
cll.insertatlast(30)
cll.insertatlast(40)
cll.insertafter(cll.search(10),50)
cll.printlist()
for x in cll:
    print(x,end=" ")
        