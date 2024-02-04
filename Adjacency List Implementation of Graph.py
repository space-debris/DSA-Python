class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[] for v in range(vno)}
        
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append[(v,weight)]
            self.adj_list[v].append[(u,weight)]
        else:
            print("invalid")
            
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex != v]
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list[v] if vertex != u]
        else:
            print("invalid")
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex,x in self.adj_list[u])
        