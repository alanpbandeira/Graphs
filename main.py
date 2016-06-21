import random, math
import graph

g = graph.Graph('test.csv')

max_cycles = math.factorial(len(g.node_data) - 1)

# print (max_cycles)
# cylces = []
# k = g.hamiltonianCycle('a')
#
# while k not in cylces:
#     cylces.append(k)
#     k = g.hamiltonianCycle('a')
#
# print ([x for x in cylces])

for line in g.costMatrix():
    print(line)

print('\n')
print g.node_list
print('\n')
print(g.nearestNeighbor())

# for y in g.edge_list:
#     print(y.incident_nodes, y.weight)
#
# for x in g.node_list:
#     x.adjacency_list.sort()
#     print(x.node_id, x.adjacency_list)
#
# for z in g.node_list:
#     print(g.node_list[z].node_id)

# v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# e = [('a', 'b'), ('a', 'c'), ('a', 'f'),
#      ('b', 'g'), ('b', 'd'), ('c', 'h'),
#      ('c', 'e'), ('d', 'i'), ('d', 'e'),
#      ('f', 'i'), ('f', 'j'), ('g', 'h'),
#      ('g', 'j'), ('i', 'h'), ('e', 'j')]
#
# def adjacencyMatrix(g_nodes):
#     mtx = []
#
#     for x in g_nodes:
#         line = []
#
#         for y in g_nodes:
#             if y.node_id in x.adjacency_list:
#                 line.append(1)
#             else:
#                 line.append(0)
#
#         mtx.append(line)
#
#     return mtx
#
#
# nodes = [node.Node(x, nodeAdjFromEdges(x, e)) for x in v]
#
# # for x in nodes:
# #     print (x.node_id)
#
# # for y in nodes:
# #     y.adjacency_list.sort()
# #     print (y.node_id, y.adjacency_list)
#
# m = adjacencyMatrix(nodes)
#
# for x in m:
#     print (x)
#
# new_e = edgesFromFile('test.csv')
# for x in new_e:
#     print (x.incident_nodes, x.weight)