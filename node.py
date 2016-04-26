from edge import Edge

class Node():
	"""docstring for Node"""
	
	adjacencency_list = list()

	def __init__(self, index):
		self.index = index

	def insertAdjacentNode(self, Node):
		self.adjacencency_list.append(Node.index)

	def removeAdjacentNode(self, Node):
		self.adjacencency_list.remove(Node.index)
		# Remover a aresta que conecta os dois vertices 



		