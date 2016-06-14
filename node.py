class Node:
    """docstring for Node"""

    adjacency_list = list()

    def __init__(self, index=None):
        self.__index = index
        self.__node_degree = None

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @index.deleter
    def index(self):
        del self.__index


    @property
    def node_degree(self):
        return self.__node_degree

    @node_degree.setter
    def node_degree(self, value):
        self.__node_degree = value

    @node_degree.deleter
    def node_degree(self):
        del self.__node_degree

    # Removes an edge that connects two vertex
    # TODO!!!

    def insertAdjacentNode(self, node):
        self.adjacency_list.append(node.index)

    def removeAdjacentNode(self, node):
        self.adjacency_list.remove(node.index)

    # Increment or decrement the node degree set on the
    # configuration of the parameter 'increase'.
    def updateNodeDegree(self, increase):
        if increase:
            self.node_degree += 1
        else:
            self.node_degree -= 1
