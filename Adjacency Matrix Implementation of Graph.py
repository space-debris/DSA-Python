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
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invald vertex")
            
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("invald vertex")
            
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list))) # row_list [0 1 0 1 ...] all elements conv to str in strfun, map function will pass elements of list in str func str(0)->"0"
            # ["0", "1","0"...] join method of str class will " ".join(list) will join elements with space
            # 0 1 0 ..
            