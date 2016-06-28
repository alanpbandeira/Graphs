import random, math
import graph

# Insert a second parameter as False to set the graph with asymmetric edges.
g = graph.Graph('data04.csv')

# for line in g.costMatrix():
# 	print (line)

# for line in sorted(g.incidence_list):
# 	fhand.write(line[0] + ' ' + line[1] + '\n')

# fhand.close()

#c_mtx = g.costMatrix()

#print('funfou')

# for line in g.costMatrix():
#     print(line)

# Run for random!
print('\n')
valid = False
while not valid:
    solution = g.randomNearestNeighbor()
    if solution:
        valid = True
        print('Solução inicial encontrada pela heurística Nearest Neighbor Insertion')
        print('Path: ', solution[0])
        print('Cost: ', solution[1])

improved_solution = g.twoOptPath(solution[0])

print('Solução encontrada pela heurística 2 - OPT sob a solução inicial')
print('Path: ', improved_solution[0])
print('Cost: ', improved_solution[1])


# Run for iterated!
# print('\n')

# solution = g.nodeNearestNeighbor()
# while solution == None:
# 	solution = g.nodeNearestNeighbor()
# print('Solução inicial encontrada pela heuística Nearest Neighbor Insertion')
# print('Path: ', solution[0])
# print('Cost: ', solution[1])

# improved_solution = g.twoOptPath(solution[0])

# print('Solução encontrada pela heuística 2 - OPT sob a solução inicial')
# print('Path: ', improved_solution[0])
# print('Cost: ', improved_solution[1])