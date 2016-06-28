# import math

# def distance(point_one, point_two):
# 	d = math.sqrt(math.pow(point_one[0] - point_two[0], 2) + math.pow(point_one[1] - point_two[1], 2))
# 	return d
	

# file_data = []
# distance_reg = {}
# coordinates = []
# fhand = open('data/Tsp280.txt', 'r')

# for line in fhand:
#     file_data.append(line)

# fhand.close()

# file_data = file_data[1:]

# for data in file_data:
# 	data = data.strip().split()
# 	coordinates.append((int(data[0]), int(data[1])))

# fhand = open('data/data04.csv', 'w')

# for i in coordinates:
# 	for j in coordinates:
# 		if i == j:
# 			continue
# 		else:
# 			coord_i = coordinates.index(i) + 1
# 			coord_j = coordinates.index(j) + 1
# 			fhand.write(str(coord_i) + ',' + str(coord_j) + ',' + str(distance(i, j)) + '\n')

# fhand.close()