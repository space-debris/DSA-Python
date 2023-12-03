class Node:
    def __init__(self,item=None,next=None): # these r local variables, we need obj instance variables
        self.item = item
        # ye obj ka isme jo val aayi wo
        self.next = next
    
class SLL:
    def __init__(self,start=None):
        self.start = start
        
    def is_empty(self):
        return self.start == None   
    
    def insert_at_start(self, data):
        n=Node(data,self.start)
        self.start = n
        
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty(): #will run if not empty
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
            
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None #list empty or item not found
    
    def insert_after(self,temp,data): #temp is the refrence after which we want to insert, we r assuming that we got temp after search function 
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            
    def delete_last(self):
        if self.start is None : #empty list
            pass
        elif self.start.next is None: #one node only
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None: #list must have atleast two nodes
                temp = temp.next
            temp.next=None        
        

#driver code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()