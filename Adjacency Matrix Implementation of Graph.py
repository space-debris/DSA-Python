class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix= [[0]*vno for e in range(vno)]
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("invald vertex")
    