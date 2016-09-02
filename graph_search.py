from node import Node
from edge import Edge
from graph import Graph

def bfs(graph, root):
	"""
	- Perform a breadth first search in a graph starting from a given root-node
	- @param: graph > A graph object.
	- @param: root  > The node_id of the starting node.
	"""

	visited = [root]
	queue = [root]

	while queue:
		current_node = queue.pop(0)
		print (current_node)

		for neightbour in graph.node_data[current_node].adjacency_list:
			if neightbour not in visited:
				visited.append(neightbour)
				queue.append(neightbour)

def dfs(graph, root):
	"""
	- Perform a depth first search in a graph from a given root-node
	- @param: graph > A graph object.
	- @param: root  > The node_id of the starting node.
	"""

	graph.node_data[root].visited = True
	print (root)

	for node in graph.node_data[root].adjacency_list:
		#print (node)
		if not graph.node_data[str(node)].visited:
			dfs(graph, node)
