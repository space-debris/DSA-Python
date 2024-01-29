class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.start=None
        self.itemcount=0
    
    def push(self,data,priority):
        nn=Node(data,priority)
        if not self.start or priority<self.start.priority:
            # covers case when list empty or priority of coming is less than the first element( would be added first)
            nn.next=self.start
            self.start = nn
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority<=priority:
                temp=temp.next
            nn.next=temp.next
            temp.next=nn
        self.itemcount +=1
        
    def is_empty(self):
        return self.start==None
    
    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        data=self.start.item
        self.start=self.start.next
        self.itemcount-=1
        return data
    
    def size(self):
        return self.itemcount

pq = PriorityQueue()
pq.push("amit",4)
pq.push("arjun",7)
pq.push("ashima",2)
pq.push("agrah",5)
pq.push("anant",8)
pq.push("ambika",1)

while not pq.is_empty():
    print(pq.pop())
