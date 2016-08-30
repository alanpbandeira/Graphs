from node import Node
from edge import Edge
from graph import graph

def breadth_first_search(root):

	visited = [root]
	queue = [root]

	while queue:
		current_node = queue.pop()
		print (current_node.node_id)

		for neightbour in current_node.adjacency_list:
			if neightbour not in visited:
				visited.append(neightbour)
				queue.append(neightbour)



