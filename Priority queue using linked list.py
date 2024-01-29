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
            