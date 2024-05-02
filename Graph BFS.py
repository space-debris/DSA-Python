class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            deqvertex = queue.pop(0)
            print(deqvertex)
            for adjacentvertex in self.gdict[deqvertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)
            
testdict={
    "a":["b","c"],
    "b":["a","d","e"],
    "c":["a","e"],
    "d":["b","e","f"],
    "e":["d","f"],
    "f":["d","e"]
}

graph = Graph(testdict)
graph.bfs("a")