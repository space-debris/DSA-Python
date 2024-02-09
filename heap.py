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
                
        
        