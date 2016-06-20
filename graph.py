from node import Node
from edge import Edge
import random


class Graph:
    """
    @:var node_list: Dictionary structure that represents the vertex set; [string node_id] : [Node node]
    @:var edge_list: List structure that represents the edge set; [Edge edge] * n_edges
    @:var incidence_list: List structure that represents the edge set using the incidence relationship between vertex;
    [(string node_id_a, string node_id_b)]
    """
    node_list = {}
    edge_list = []
    incidence_list = []

    def __init__(self, file_name):
            self.graphFromFile(file_name)

    def graphFromFile(self, file_name):
        """
        - Instantiate a graph from a csv file
        -
        @:param file_name: String - name of the file to be read. It must be an .csv file.
        """
        path = 'data/' + file_name
        fhand = open(path, 'r')

        for line in fhand:
            line = line.strip().split(',')
            self.edge_list.append(Edge((line[0], line[1]), int(line[2])))
            self.incidence_list.append((line[0], line[1]))

        fhand.close()

        fhand = open(path, 'r')
        for line in fhand:
            line = line.strip().split(',')

            if line[0] not in self.node_list:
                self.node_list[line[0]] = (Node(line[0], self.setNodeAdj(line[0])))
            if line[1] not in self.node_list:
                self.node_list[line[1]] = (Node(line[1], self.setNodeAdj(line[1])))

    def setNodeAdj(self, node_id):
        """
        - Provides the adjacency list of a node from a list of edges.
        -
        :param node_id: The id that identify the node from which the adjacency list will be draw.
        :return a_list: a list of adjacent nodes of the node_id
        """
        a_list = []

        for edge in self.edge_list:
            if node_id in edge.incident_nodes:
                if node_id is edge.incident_nodes[0]:
                    a_list.append(edge.incident_nodes[1])
                else:
                    a_list.append(edge.incident_nodes[0])

        return a_list


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# - MATRIX OPERATIONS
#
# -> Adjacency Matrix
# -> Cost Matrix
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def adjacencyMatrix(self):
        """
        - Create the adjacency matrix of the graph
        -
        :return mtx: A two dimensional array  info of the graph adjacency.
        """
        mtx = []
        nodes = sorted(self.node_list)

        for node_x in nodes:
            line = []

            for node_y in nodes:
                if node_y in self.node_list[node_x].adjacency_list:
                    line.append(1)
                else:
                    line.append(0)

            mtx.append(line)

        return mtx

    def costMatrix(self, minimize=True):
        """
        - Create the adjacency matrix of the graph
        -
        :return mtx: A two dimensional array  info of the graph adjacency.
        """
        mtx = []
        nodes = sorted(self.node_list)

        for node_x in nodes:
            line = []

            for node_y in nodes:
                if (node_y, node_x) in self.incidence_list:
                    line.append(self.edge_list[self.incidence_list.index((node_y, node_x))].weight)
                elif (node_x, node_y) in self.incidence_list:
                    line.append(self.edge_list[self.incidence_list.index((node_x, node_y))].weight)
                else:
                    if minimize:
                        line.append(9999)
                    else:
                        line.append(-1)

            mtx.append(line)

        return mtx


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# - PATH OPERATIONS
#
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def hamiltonianCycle(self, start, cycle=False):
        path = []

        elected = start
        next_node = random.choice(self.node_list[elected].adjacency_list)

        while next_node is not start and next_node not in path:
            path.append(elected)
            elected = next_node

            next_node = random.choice(self.node_list[elected].adjacency_list)

            print (next_node)

        path.append(start)

        return path










































