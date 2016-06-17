import node
import edge
import random

class Graph:
    """

    """
    node_list = None
    edge_list = None

    def __init__(self, file_name):
            self.edgesFromFile(file_name)

    def edgesFromFile(self, file_name):
        path = 'data/' + file_name

        fhand = open(path, 'r')

        for line in fhand:
            line = line.split(',')
            self.edge_list.append(edge.Edge((line[0], line[1]), line[2]))

    def nodesFromEdges(self):
        for edge in self.edge_list:


    def setNodeAdj(self, elected_node):
        """
        Provides the adjacency list of a node from a list of edges.
        :param elected_node:
        :return a_list: a list of adjacent nodes of the elected_node
        """
        a_list = []

        for t in self.edge_list:
            if elected_node.node_id in t.incident_nodes:
                if elected_node is t.incident_nodes[0]:
                    a_list.append(t.incident_nodes[1])
                else:
                    a_list.append(t.incident_nodes[0])

        return a_list

    def adjacencyMatrix(self):
        """
        Create the adjacency matrix of the graph
        :return mtx: A two dimensional array  info of the graph adjacency.
        """
        mtx = []

        for node_x in self.node_list:
            line = []

            for node_y in self.node_list:
                if node_y.node_id in node_x.adjacency_list:
                    line.append(1)
                else:
                    line.append(0)

            mtx.append(line)

        return mtx