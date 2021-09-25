import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt

fil = open("/home/ec2-user/environment/code/week9_graphs/zoomsession2/edges.txt")

g = nx.DiGraph()
edges = []
for line in fil.readlines():
    n1, n2, e  = line.split(",")
    e = int(e)
    edges.append((n1, n2, e))
print(edges)
g.add_weighted_edges_from(edges) 

# nx.draw(g, with_labels=True)

pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("graph.png")

print(g.nodes)
# input()
for n1, n2 in permutations(g.nodes,2):
    print("paths from",n1,"to",n2,":")
    shortest_path_weight = 99999999999
    shortest_path = []
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path)
        path_weight = 0
        for i in range(len(path)-1):
            print("path from",path[i],"to",path[i+1],": ",g[path[i]][path[i+1]]["weight"])
            path_weight += g[path[i]][path[i+1]]["weight"]
        print(path, "weight is: ", path_weight)
        if path_weight < shortest_path_weight:
            shortest_path_weight = path_weight
            shortest_path = path
    
    print("shortest path from", n1, "to", n2, "is: ", shortest_path, "of weight: ", shortest_path_weight)
        
        
        
print(0)