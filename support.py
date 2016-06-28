fhand = open('data/Tsp58.txt', 'r')
data_lines = [] 

for line in fhand:
	data_lines.append(line.strip().split())

fhand.close()

data_lines = data_lines[1:]
# data = {}

# for line in data_lines:
# 	for index in range((data_lines.index(line)+1), len(line), 1):
# 		data[(data_lines.index(line), index)] = line[(data_lines.index(line) len)]

# print (data)

fhand = open('data/data05.csv', 'w')

for node_x in data_lines:
	for node_y in node_x:
		edge_a = data_lines.index(node_x) + 1
		edge_b = node_x.index(node_y) + 1 + edge_a
		fhand.write(str(edge_a) + ',' + str(edge_b) + ',' + str(node_y) + '\n')
		node_x[node_x.index(node_y)] = None

fhand.close()

