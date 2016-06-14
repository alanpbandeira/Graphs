class Edge:
    """docstring for Edge"""

    def __init__(self, free_element=False, nodes=None, weight=None, edge_id=None):
        self.__e_id = edge_id
        self.__weight = weight

        if free_element:
            self.__incident_nodes = None
        else:
            self.incidentNodes(nodes)

    @property
    def incidentNodes(self):
        return self.__incident_nodes

    @incidentNodes.setter
    def incidentNodes(self, nodes):
        """
        Sets the incidents nodes of an edge and updates the nodes
        attributes adjacency list and degree.

        :param nodes: tuple of Node elements
        :return void:
        """
        self.__incident_nodes = nodes

        nodes[0].insertAdjacentNode(nodes[1])
        nodes[1].insertAdjacentNode(nodes[0])

        nodes[0].updateDegree()
        nodes[1].updateDegree()

    @incidentNodes.deleter
    def incidentNodes(self):
        del self.__incident_nodes

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @weight.deleter
    def weight(self):
        del self.__weight

    @property
    def e_id(self):
        return self.e_id

    @e_id.setter
    def e_id(self, value):
        self.e_id = value

    @e_id.deleter
    def e_id(self):
        del self.e_id
