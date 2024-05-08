class Graph:
	def __init__(self):
		self.adjacency_list = {}
		
	def add_edge(self,u,v):
		if u not in self.adjacency_list:
			self.adjacency_list[u]=[]
		if v not in self.adjacency_list:
			self.adjacency_list[v]=[]	
		self.adjacency_list[u].append(v)
		self.adjacency_list[v].append(u)
		
	def dfs(self,vertex,visited=None):
		if visited is None:
			visited = set()
		visited.add(vertex)
		print(vertex,end=' ')
		for neighbor in self.adjacency_list[vertex]:
			if neighbor not in visited:
				self.dfs(neighbor,visited)
				
	def bfs(self,queue,visited=None):
		if queue==[]:
			return
		vertex = queue.pop(0)
		print(vertex,end=' ')
		if visited is None:
			visited = set()
		visited.add(vertex)
		for neighbor in self.adjacency_list[vertex]:
			if neighbor not in visited:
				queue.append(neighbor)
		self.bfs(queue,visited)
				
	
g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,6)

print("\nDFS order is:")
g.dfs(0)
print("\nBFS ORDER IS:")
g.bfs([0])
	
	
