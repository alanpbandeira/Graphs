import sys


class Node(object):

    def __init__(self, node_id, adjacency_list):
        """
        Defines the Node model for an graph.
        :param node_id: String - Element that identify a node.
        :param adjacency_list:
        """
        self.node_id = node_id
        self.adjacency_list = adjacency_list
        self.degree = len(adjacency_list)
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize

    def __cmp__(self, other_node):
        return self.cmp(self.min_distance, other_node.min_distance)

    def __lt__(self, other):
        self_priotity = self.min_distance
        other_priority = other.min_distance
        return self_priotity < other_priority