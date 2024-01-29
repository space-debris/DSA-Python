#smaller num => more priority
#in pylist items automatically shift to next index

class PriorityQueue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
        
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index +=1
        self.items.insert(index,(data,priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
            
pq = PriorityQueue()
pq.push("amit",4)
pq.push("arjun",7)
pq.push("ashima",2)
pq.push("agrah",5)
pq.push("anant",8)
pq.push("ambika",1)

while not pq.is_empty():
    print(pq.pop())

            