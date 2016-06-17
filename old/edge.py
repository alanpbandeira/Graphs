class Edge:
    """docstring for Edge"""

    def __init__(self, incident_nodes, weight=None, edge_id=None):
        self.__e_id = edge_id
        self.__weight = weight
        self.__incident_nodes = incident_nodes

        self.incidentNodes()

    @property
    def incidentNodes(self):
        return self.__incident_nodes

    @incidentNodes.setter
    def incidentNodes(self):
        """
        Sets the incidents nodes of an edge and updates the nodes
        attributes adjacency list and degree.

        :param nodes: tuple of Node elements
        :return void:
        """

        self.incidentNodes()[0].insertAdjacentNode(self.incidentNodes()[1])
        self.incidentNodes()[1].insertAdjacentNode(self.incidentNodes()[0])

        self.incidentNodes()[0].updateDegree()
        self.incidentNodes()[1].updateDegree()

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
