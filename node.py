class Node:

    def __init__(self, node_id, adjacency_list):
        """
        Defines the Node model for an graph.
        :param node_id: String - Element that identify a node.
        :param adjacency_list:
        """
        self.node_id = node_id
        self.adjacency_list = adjacency_list
        self.degree = len(adjacency_list)