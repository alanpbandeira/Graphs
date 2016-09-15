import heapq


def shortestPath(graph, start_node):
	"""
	- @Info: Calculate the shortes path between two nodes of the graph.
	- @param: node_list  > List of the graph nodes.
	- @param: start_node > Starting node of the path.
	"""
	
	queue = []
	graph.node_data[start_node].min_distance = 0
	heapq.heappush(queue, start_node)

	while len(queue) > 0:
		
		acutal_vertex = heapq.heappop(queue)

		for node in graph.node_data[acutal_vertex].adjacency_list:
			new_distance = graph.node_data[acutal_vertex].min_distance + graph.edge_data[(acutal_vertex, node)].weight

			if new_distance < graph.node_data[node].min_distance:
				graph.node_data[node].predecessor = acutal_vertex
				graph.node_data[node].min_distance = new_distance
				heapq.heappush(queue, node)

def shortestPathTo(graph, target_vertex):
	
	print ("Shortest path to target is: ", graph.node_data[target_vertex].min_distance)

	node = target_vertex

	while node is not None:
		print (str(graph.node_data[node].node_id) + " -> ")
		node = graph.node_data[node].predecessor