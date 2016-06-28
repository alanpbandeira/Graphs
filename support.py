fhand = open('data/Tsp58.txt', 'r')
data_lines = [] 

for line in fhand:
	data_lines.append(line.strip().split())

fhand.close()

