

class Edge(object):
    """

    """

    def __init__(self, incident_nodes, weight):
    	"""
    	@param: inicident_nodes > Tuple of node_id strings
    	@param: weight > Numeric value(int or float) indicating the edge weight

    	"""
    	self.incident_nodes = incident_nodes
    	self.weight = weight
        

