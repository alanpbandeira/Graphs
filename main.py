import random, math
import node, edge, graph

v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

e = [('a', 'b'), ('a', 'c'), ('a', 'f'),
     ('b', 'g'), ('b', 'd'), ('c', 'h'),
     ('c', 'e'), ('d', 'i'), ('d', 'e'),
     ('f', 'i'), ('f', 'j'), ('g', 'h'),
     ('g', 'j'), ('i', 'h'), ('e', 'j')]


def edgesFromFile(file_name):
    path = 'data/' + file_name

    fhand = open(path, 'r')
    edge_list = []

    for line in fhand:
        line = line.split(',')
        edge_list.append(edge.Edge((line[0], line[1]), line[2]))

    return edge_list


def nodeAdjFromEdges(elected_node, edge_list):
    a_list = []

    for t in edge_list:
        if elected_node in t:
            if elected_node is t[0]:
                a_list.append(t[1])
            else:
                a_list.append(t[0])

    return a_list


def adjacencyMatrix(g_nodes):
    mtx = []

    for x in g_nodes:
        line = []

        for y in g_nodes:
            if y.node_id in x.adjacency_list:
                line.append(1)
            else:
                line.append(0)

        mtx.append(line)

    return mtx


nodes = [node.Node(x, nodeAdjFromEdges(x, e)) for x in v]

# for x in nodes:
#     print (x.node_id)

# for y in nodes:
#     y.adjacency_list.sort()
#     print (y.node_id, y.adjacency_list)

m = adjacencyMatrix(nodes)

for x in m:
    print x

new_e = edgesFromFile('test.csv')
for x in new_e:
    print x.incident_nodes, x.weight