from node import Node
from edge import Edge


class Graph:
    """docstring for Graph"""

    __graph_order = None
    __graph_size = None

    def __init__(self, edge_list=None, node_list=None):
        self.edges = edge_list
        self.nodes = node_list

    def adjacencyMatrix(self):
        mtx = [[0 for x in range(len(self.nodes))] for y in range(len(self.nodes))]

        for x in mtx:
            for y in x:
                if y.index() in x.adjacency_list:
                    mtx[mtx.index(x)][mtx.index(y)] = 1

        return mtx

    def createNode(self, index, rand=False):
        if rand:
            pass
        else:
            self.nodes.append(Node(index))

    def insertNode(self, new_node, adjacent_node, rand=False):
        if rand:
            pass
        else:
            new_edge = Edge()
            new_edge.incidentNodes((new_node, adjacent_node))
            self.edges.append

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

