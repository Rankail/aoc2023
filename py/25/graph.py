
# visualizes the graph-file

import matplotlib.pyplot as plt
import networkx as nx
import pyvis as pv

graph = nx.Graph()

nodes = set()
edges = set()

with open("graph.txt", "r") as f:
    for line in f.read().split("\n"):
        if len(line) == 0: continue
        edge = tuple(line.split(" "))
        nodes.add(edge[0])
        nodes.add(edge[1])
        edges.add(edge)

graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

nx.draw(graph, with_labels=True)
plt.show()
exit()

# this loades for ~1min :(
g = pv.network.Network(width="99vw", height="98vh",
                       bgcolor="#222222", font_color="white")
g.from_nx(graph)
g.force_atlas_2based(gravity=-30)
g.show("graph.html", notebook=False)