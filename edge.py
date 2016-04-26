from node import Node

class Edge():
	"""docstring for Edge"""

	incident_nodes = None

	def __init__(self, e_id, weight, Node_a, Node_b):
		self.e_id   = e_id
		self.weight = weight
		slef.setIncident(Node_a, Node_b)

	def setIncident(self, Node_a, Node_b):
		self.incident_nodes = (Node_a.index, Node_b.index)
		Node_a.insertAdjacentNode(Node_b)
		Node_b.insertAdjacentNode(Node_a)