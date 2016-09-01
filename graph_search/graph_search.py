from node import Node
from edge import Edge
from graph import graph

def breadth_first_search(graph, root):

	visited = [root]
	queue = [root]

	while queue:
		current_node = queue.pop()
		print (current_node)

		for neightbour in graph.node_data[root].adjacency_list:
			if neightbour not in visited:
				visited.append(neightbour)
				queue.append(neightbour)



