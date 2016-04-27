from edge import Edge

class Node():
	"""docstring for Node"""
	
	adjacencency_list = list()
	node_degree = None

	def __init__(self, index):
		self.index = index

	def insertAdjacentNode(self, Node):
		self.adjacencency_list.append(Node.index)

	def removeAdjacentNode(self, Node):
		self.adjacencency_list.remove(Node.index)
		# Remover a aresta que conecta os dois vertices

	def setNodeDegree(self, value):
		self.node_degree = value

	# Increment or decrement the node dregree set on the 
	# configuration of the parameter 'increase'.
	def updateNodeDegree(self, increase):
		if increase:
			self.node_degree += 1
		else:
			self.node_degree -= 1




		