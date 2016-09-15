import graph
#import GraphSearch.graph_search as gs
import Dijkstra.short_path as dj


# Insert a second parameter as False to set the graph with asymmetric edges.
g = graph.Graph('test.csv')

dj.shortestPath(g, str(1))
dj.shortestPathTo(g, str(1))