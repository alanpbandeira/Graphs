import graph
import GraphSearch.graph_search as gs


# Insert a second parameter as False to set the graph with asymmetric edges.
g = graph.Graph('test.csv')

gs.bfs(g, str(1))