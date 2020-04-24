class GraphMatrix:
    def __init__(self,vertices):
        self.matrix = [[0]*vertices for _ in range(vertices)]
        self.vertices = vertices
        self.visited = [0]*vertices

    def add_edge(self,v1,v2,w=1):
        self.matrix[v1][v2] = w
        self.matrix[v2][v1] = w

    def remove_edge(self,v1,v2):
        self.matrix[v1][v2] = 0
        self.matrix[v1][v2] = 0

    def DFS(self,source):
        if self.visited[source] == 0:
            print(source, end="-")
            self.visited[source] = 1
            for j in range(self.vertices):
                if self.matrix[source][j] == 1 and self.visited[j] == 0:
                    self.DFS(j)

    def BFS(self,source):
        queue = []
        queue.append(source)
        print(source,end="-")
        self.visited[source] = 1
        while queue:
            pop_elem = queue.pop(0)
            for j in range(self.vertices):
                if self.matrix[pop_elem][j] == 1 and self.visited[j] == 0:
                    print(j,end="-")
                    self.visited[j] = 1
                    queue.append(j)


#Driver Code
g = GraphMatrix(6)
g.add_edge(0,1)
g.add_edge(0,5)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,1)
g.add_edge(4,0)
g.add_edge(4,5)

print(g.matrix)
#g.DFS(0)
#g.BFS(0)

        
