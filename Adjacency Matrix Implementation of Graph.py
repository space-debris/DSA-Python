class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix= [[0]*vno for e in range(vno)]
    
    def add_edge(self,u,v,weight=1):
        