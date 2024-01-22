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
        
    def insertafter(self, temp, data):
        if temp is not None:
            nn = Node(temp.prev, data, temp)
            if temp.prev is not None:
                temp.prev.next = nn
            else:
                self.start = nn
            temp.prev = nn
        
    def printall(self):
        temp = self.start
        if temp is not None:
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
     
    def deletefirst(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    
    def deletelast(self):
        if self.start is None:
            pass
        elif self.start.next == None:
            #single node only 
            self.start = None
        else:
            temp = self.start
            while temp is not None:
                temp = temp.next
            temp.prev.next = None
        
    def deleteitem(self,data):
        if self.start is None:
            pass
        else :
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else :
                        self.start = temp.next
                    break
                temp = temp.next
                
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:    
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current : 
            raise StopIteration
        data =  self.current.item
        self.current = self.current.next
        return data
    
dll = DLL()
dll.insertatlast(52)
dll.insertatstart(25)
dll.insertafter(dll.search(52),72)
dll.insertafter(dll.search(25),32)
dll.printall()
print()
for x in dll:
    print(x,end=" ")
            