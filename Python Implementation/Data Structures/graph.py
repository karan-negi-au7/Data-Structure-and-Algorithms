from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph_dict = defaultdict(list)

    def addEdge_u(self,ver_a,ver_b):
        self.graph_dict[ver_a].append(ver_b)
        self.graph_dict[ver_b].append(ver_a) 

    def addEdge_d(self,ver_a,ver_b):
        self.graph_dict[ver_a].append(ver_b)

    def dfs(self,start):
        self.visited = [False]*len(self.graph_dict)
        self.dfs_runner(start) 

    def dfs_runner(self,start):
        self.visited[ord(start)-65] = True
        print(start,"",end="")
        for i in self.graph_dict[start]:
            if self.visited[ord(i)-65] == False:
                self.dfs_runner(i)           
    
    def BFS(self,start):
        self.visited = [False]*len(self.graph_dict)
        queue = [start]
        self.visited[ord(start)-65] = True
        while queue:
            start = queue.pop(0)
            print(start,"",end="") 
            for i in self.graph_dict[start]:
                if self.visited[ord(i)-65] == False:
                    self.visited[ord(i)-65] = True
                    queue.append(i)


    #check if there is path exist b/w 2 nodes
    def path_check(self,start,e):
        self.visited = [False]*len(self.graph_dict)
        self.path_check_runner(start,e) 

    def path_check_runner(self,start,e):
        self.visited[ord(start)-65] = True
        print(start,"",end="")
        if start == "E":
            return
        for i in self.graph_dict[start]: 
            if self.visited[ord(i)-65] == False:
                self.dfs_runner(i) 
                 
g = Graph()        
g.addEdge_u("A","B")
g.addEdge_u("A","C") 
g.addEdge_u("B","D") 
g.addEdge_u("B","E")
g.addEdge_u("C","E")
g.addEdge_u("D","E")
g.addEdge_u("D","F")
g.addEdge_u("E","F")

#print(g.graph_dict)
#g.path_check("B","E")
g.BFS("D")
