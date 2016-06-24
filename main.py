import random, math
import graph

# Insert a second parameter as False to set the graph with asymmetric edges.
g = graph.Graph('data03.csv')

for line in g.costMatrix():
    print(line)

# Working!
print('\n')
valid = False
count = 0

while not valid:
    solution = g.nearestNeighbor()
    if solution:
        valid = True
        print('Solução inicial encontrada pela heuística Nearest Neighbor Insertion')
        print('Path: ', solution[0])
        print('Cost: ', solution[1])

improved_solution = g.twoOptPath(solution[0])

print('Solução encontrada pela heuística 2 - OPT sob a solução inicial')
print('Path: ', improved_solution[0])
print('Cost: ', improved_solution[1])
