from node import Node
from edge import Edge
import random


class Graph(object):
    """
    @:var node_list: Dictionary; [string node_id] : [Node node]
    @:var edge_list: List; [Edge edge] * n_edges
    @:var incidence_list: List;
    [(string node_id_a, string node_id_b)]
    """
    node_data = {}
    node_list = []
    edge_data = {}
    incidence_list = []

    def __init__(self, file_name, symmetric=True):
        self.symmetric_mtx = symmetric
        self.graphFromFile(file_name)

    def graphFromFile(self, file_name):
        """
        - Instantiate a graph from a csv file
        -
        @:param file_name: String - name of the file to be read. It must be an .csv file.
        """
        path = 'data/' + file_name
        fhand = open(path, 'r')
        
        # Construct
        for line in fhand:
            line = line.strip().split(',')
            if self.symmetric_mtx:
                try:
                    self.edge_data[(line[0], line[1])] = Edge((line[0], line[1]), int(line[2]))
                    self.edge_data[(line[1], line[0])] = Edge((line[1], line[0]), int(line[2]))
                except ValueError:
                    self.edge_data[(line[0], line[1])] = Edge((line[0], line[1]), float(line[2]))
                    self.edge_data[(line[1], line[0])] = Edge((line[1], line[0]), float(line[2]))
            else:
                try:
                    self.edge_data[(line[0], line[1])] = Edge((line[0], line[1]), int(line[2]))
                except ValueError:
                    self.edge_data[(line[0], line[1])] = Edge((line[0], line[1]), float(line[2]))

        fhand.close()

        self.incidence_list = [x for x in self.edge_data]

        fhand = open(path, 'r')
        for line in fhand:
            line = line.strip().split(',')
            if line[0] not in self.node_data:
                self.node_data[line[0]] = (Node(line[0], self.setNodeAdj(line[0])))
            if line[1] not in self.node_data:
                self.node_data[line[1]] = (Node(line[1], self.setNodeAdj(line[1])))
        fhand.close()

        self.node_list = sorted([int(x) for x in self.node_data])

    def setNodeAdj(self, node_id):
        """
        - Provides the adjacency list of a node from a list of edges.
        -
        :param node_id: The id that identify the node from which the adjacency list will be draw.
        :return a_list: a list of adjacent nodes of the node_id
        """
        a_list = []

        for edge in self.incidence_list:
            if node_id in edge:
                if node_id == edge[0]:
                    a_list.append(edge[1])
                else:
                    a_list.append(edge[0])

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

        for node_x in self.node_list:
            line = []
            for node_y in self.node_list:
                if str(node_x) in self.node_data[str(node_y)].adjacency_list:
                    line.append(1)
                else:
                    line.append(0)
            mtx.append(line)

        return mtx

    def relativeCostMatrix(self, minimize=True):
        a = self.adjacencyMatrix()
        mtx = []

        for node_x in a:
            line = []
            for node_y in node_x:
                if node_x[node_x.index(node_y)] == 1:
                    cost = self.edge_data[(str((a.index(node_x)+1)), str((node_x.index(node_y)+1)))].weight
                    #print (cost)
                    line.append(cost)
                else:
                    if minimize:
                        line.append(9999)
                    else:
                        line.append(-1)
            mtx.append(line)

        return mtx

    def costMatrix(self, minimize=True):
        """
        - Create the adjacency matrix of the graph
        -
        :return mtx: A two dimensional array  info of the graph adjacency.
        """
        mtx = []

        if self.symmetric_mtx:  # Build a symmetric cost matrix using the edges weight
            for node_x in self.node_list:
                line = []
                for node_y in self.node_list:
                    if (str(node_x), str(node_y)) in self.incidence_list:
                        line.append(self.edge_data[(str(node_x), str(node_y))].weight)
                    elif (str(node_y), str(node_x)) in self.incidence_list:
                        line.append(self.edge_data[(str(node_y), str(node_x))].weight)
                    else:
                        if minimize:
                            line.append(9999)
                        else:
                            line.append(-1)

                mtx.append(line)
        else:  # Build an asymmetric cost matrix using the edges weight
            for node_x in self.node_list:
                line = []
                for node_y in self.node_list:
                    if (str(node_x), str(node_y)) in self.incidence_list:
                        line.append(self.edge_data[(str(node_x), str(node_y))].weight)
                    # if (str(node_x), str(node_y)) in self.incidence_list:
                    #     line.append(self.edge_data[(str(node_x), str(node_y))].weight)
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

    def randomNearestNeighbor(self):
        """
        - Build a minimum path using the Nearest Neighbor heuristic sed to solve the TSP
        - but do not guarantee optimal solution.
        :return path, path_cost: The path found and it's cost
        """
        path = []
        path_cost = 0
        c_mtx = self.costMatrix(True)

        first_node = elected_node = c_mtx.index(random.choice(c_mtx))
        # print(elected_node)
        path.append(self.node_list[elected_node])

        while len(path) <= len(self.node_list):
            candidate_value = min(c_mtx[elected_node])
            if candidate_value == 9999:
                path_cost += self.edge_data[(str(path[len(path) - 1]), str(self.node_list[first_node]))].weight
                path.append(self.node_list[first_node])
                break
            candidate_node = self.randomMultiIndex(c_mtx[elected_node], candidate_value)
            if self.node_list[candidate_node] in path:
                c_mtx[elected_node][candidate_node] = 9999
                continue
            else:
                path.append(self.node_list[candidate_node])
                path_cost += candidate_value
                # print(elected_node, candidate_node, path_cost)
                elected_node = candidate_node

        if len(path) <= len(self.node_list):
            # print("Non-Hamiltonian path found")
            print (path)
            return False
        else:
            return path, path_cost

    def nodeNearestNeighbor(self, symmetric=True):
        """
        - Build a minimum path using the Nearest Neighbor heuristic sed to solve the TSP
        - but do not guarantee optimal solution.
        :return path, path_cost: The path found and it's cost
        """

        for node in self.node_list:
            path = []
            path_cost = 0
            c_mtx = self.relativeCostMatrix(True)
            first_node = elected_node = self.node_list.index(node)
            # print(elected_node)
            path.append(self.node_list[elected_node])

            while len(path) <= len(self.node_list):
                candidate_value = min(c_mtx[elected_node])
                if candidate_value == 9999:
                    if path[len(path) - 1] == self.node_list[first_node]:
                        break
                    else:
                        path_cost += self.edge_data[(str(path[len(path) - 1]), str(self.node_list[first_node]))].weight
                        path.append(self.node_list[first_node])
                        break
                candidate_node = self.randomMultiIndex(c_mtx[elected_node], candidate_value)
                if self.node_list[candidate_node] in path:
                    c_mtx[elected_node][candidate_node] = 9999
                    continue
                else:
                    path.append(self.node_list[candidate_node])
                    path_cost += candidate_value
                    # print(elected_node, candidate_node, path_cost)
                    elected_node = candidate_node

            if len(path) <= len(self.node_list):
                # print("Non-Hamiltonian path found")
                print (path)
                continue
            else:
                return path, path_cost

    def pathCost(self, path):
        cost = 0

        for node_x, node_y in zip(path[:len(path) - 1], path[1:]):
            cost += self.edge_data[str(node_x), str(node_y)].weight

        return cost

    def twoOptPath(self, path):
        current_path = path
        current_cost = self.pathCost(path)
        print('\n')

        for node_x in current_path[1:len(path) - 2]:
            index_x = current_path.index(node_x)

            candidate_path = current_path[:index_x] + [current_path[index_x + 1], current_path[index_x]] + current_path[index_x+2:]

            candidate_cost = self.pathCost(candidate_path)
            if candidate_cost < current_cost:
                current_path = candidate_path
                current_cost = candidate_cost
                print('Nova melhor solução')
                print('Path: ', current_path)
                print('Cost: ', current_cost)
            else:
                continue

        # for node_x, node_y in zip(current_path[1:len(path)-2], current_path[2:len(path)-1]):
        #     index_x = current_path.index(node_x)
        #     index_y = current_path.index(node_y)
        #     print (index_x, index_y)
        #     candidate_path = current_path[:index_x] + [node_y] + [node_x] + current_path[index_y+1:]
        #     candidate_cost = self.pathCost(candidate_path)
        #     #print (candidate_cost)
        #     if candidate_cost < current_cost:
        #         current_path = candidate_path
        #         current_cost = candidate_cost
        #         print('Nova melhor solução')
        #         print('Path: ', current_path)
        #         print('Cost: ', current_cost)
        #     else:
        #         continue

        return current_path, current_cost

    def nearestInsertionPath(self, symmetric=True):
        """
        TOFINISH!!!
        :param symmetric:
        :return:
        """
        path = []
        path_cost = 0
        c_mtx = self.costMatrix(True, symmetric)

        # Build the first inner cycle
        elected_node = c_mtx.index(random.choice(c_mtx))
        print(elected_node)
        path.append(self.node_list[elected_node])
        candidate_value = min(c_mtx[elected_node])
        candidate_node = c_mtx[elected_node].index(candidate_value)
        path.append(self.node_list[candidate_node])
        path.append(self.node_list[elected_node])

        c_mtx[elected_node][candidate_node] = 9999
        c_mtx[candidate_node][elected_node] = 9999

        while len(path) < len(self.node_list):
            # select the nearest node
            nearest_node = None
            nearest_node_value = None
            for node in path[:(len(path) - 1)]:
                print(nearest_node)
                candidate_value = min(c_mtx[self.node_list.index(node)])
                candidate_node = c_mtx[self.node_list.index(node)].index(candidate_value)
                if nearest_node is None or nearest_node_value > candidate_value:
                    nearest_node = candidate_node
                    nearest_node_value = candidate_value
                else:
                    continue

            # select the elected position
            delta_path = None
            position = None
            candidate_position = 1
            for node in path[:(len(path) - 1)]:
                edge_a = self.edge_data[(str(node), str(self.node_list[nearest_node]))].weight
                # edge_a = c_mtx[self.node_list.index(node)][self.node_list.index(nearest_node)]
                edge_b = self.edge_data[str(self.node_list[nearest_node]), str(path[candidate_position])].weight
                # edge_b = c_mtx[self.node_list.index(nearest_node)][self.node_list.index(path[candidate_position])]
                edge_c = self.edge_data[(str(node), str(path[candidate_position]))].weight
                # edge_c = c_mtx[self.node_list.index(node)][self.node_list.index(candidate_position)]

                position_delta = edge_a + edge_b - edge_c

                if delta_path is None or position_delta < delta_path:
                    delta_path = position_delta
                    position = candidate_position
                    candidate_position += 1
                else:
                    candidate_position += 1
                    continue

            path = path[:position] + [self.node_list[nearest_node]] + path[position:]

            c_mtx[self.node_list.index(path[position - 1])][self.node_list.index(path[position])] = 9999
            c_mtx[self.node_list.index(path[position])][self.node_list.index(path[position - 1])] = 9999
            c_mtx[self.node_list.index(path[position])][self.node_list.index(path[position + 1])] = 9999
            c_mtx[self.node_list.index(path[position + 1])][self.node_list.index(path[position])] = 9999

        # print(self.node_list[nearest_node], nearest_node_value)

        return path

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # - STATIC METHODS
    #
    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    @staticmethod
    def randomMin(array):
        min_candidates = [array[0]]
        for element in array[1:]:
            if element == min(min_candidates):
                min_candidates.append(element)
            elif element < min(min_candidates):
                elements = len(min_candidates)
                min_candidates = [element for x in range(elements)]
            else:
                continue

        return random.choice(min_candidates)

    @staticmethod
    def randomMultiIndex(array, value):
        """
        Select randomly a index of an array of similar values using the value as a parameter.
        :return index:
        """
        candidate_indexes = []
        dull_array = array

        for element in dull_array:
            if element == value:
                index = dull_array.index(element)
                candidate_indexes.append(index)
                dull_array[index] = 9999

        return random.choice(candidate_indexes)
