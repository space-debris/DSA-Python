class Heap:
    
    def __init__(self):
        self.heap=[]
    
    def createheap(self,list1):
        for e in list1:
            self.insert(e)
    
    def insert(self,e):
        index=len(self.heap) # say 0-4 so 5th would be new index #adding at last
        parent=(index-1)/2
        while index>0 and self.heap[parent]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parent])
            else:
                self.heap[index]=self.heap[parent]
            
            index=parent
            parent=(index-1)/2
        
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
            
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]

class EmptyHeapException(Exception):
    def __init__(self,msg="empty heap"):
        self.msg=msg
    def __str__(self):
        return self.msg        