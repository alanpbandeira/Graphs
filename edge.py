from node import Node

class Edge():
	"""docstring for Edge"""

	incident_nodes = None
	weight = None

	def __init__(self, e_id, weight, Node_a, Node_b):
		self.e_id   = e_id
		self.weight = weight
		slef.setIncident((Node_a, Node_b))

	def setIncidentNodes(self, nodes):
		self.incident_nodes = (nodes[0].index, nodes[1].index)
		nodes[0].insertAdjacentNode(nodes[1])
		nodes[1].insertAdjacentNode(nodes[0])

		nodes[0].updateDegree()
		nodes[1].updateDegree()

	def delIncidentNodes(self):
		self.incident_nodes = None

	def setWeight(self, value):
		self.weight = value