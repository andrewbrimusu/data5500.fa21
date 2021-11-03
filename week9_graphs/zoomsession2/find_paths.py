import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations


import os
# os.system("sudo pip install networkx")
# os.system("sudo apt-get install libjpeg-dev zlib1g-dev")
# os.system("sudo pip install Pillow")
# os.system("sudo pip3 install matplotlib")

import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.function import path_weight

file = open("/home/ubuntu/environment/data5500.fa21/week9_graphs/zoomsession2/edges.txt")

g = nx.DiGraph()

# STEP 1
# get all edges from the txt file
edges = []

for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = int(weight)
    edges.append((node1, node2, weight))
    
print(edges)
# g.add_weighted_edges_from(edges) 
for e in edges:
    g.add_edge(e[0], e[1], weight=e[2])

# print all nodes
print(g.nodes)

#for fun, you can save an image of your graph
pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("graph.png")


# STEP 2
# for each node pair, find paths between them
for n1, n2 in permutations(g.nodes,2): #permutations returns all pairs
    # print("paths from",n1,"to",n2,":")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        # do something
        if n1 == "v0" and n2 == "v5":
            print(path)
            path_weight = 0
            for i in range(len(path) - 1):
                path_weight += g[path[i]][path[i+1]]['weight']
            print("path_weight: ", path_weight)