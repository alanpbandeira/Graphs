from node import Node
from edge import Edge


class Graph:
    """docstring for Graph"""

    edge_list = list()
    node_list = list()

    __graph_order = None
    __graph_size = None

    def __init__(self, edge_list, node_list):
        self.edge_list = edge_list
        self.node_list = node_list

    def createNode(self, rand=False):
        pass

    def insertNode(self, new_node, adjacent_node, rand=False):
        if rand:
            pass
        else:
            new_edge = Edge()
            new_edge.incidentNodes((new_node, adjacent_node))
            self.edge_list.append

    def removeNode(self, node_index):
        pass

    def removeEdge(self, edge_id):
        pass

    def createAdjacencyMatrix(self):
        pass

    def createCostMatrix(self):
        pass

    def createDistanceMatrix(self):
        pass

