import graph
import graph_search as gs

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

# Insert a second parameter as False to set the graph with asymmetric edges.
g = graph.Graph('data03.csv')

gs.dfs(g, str(1))