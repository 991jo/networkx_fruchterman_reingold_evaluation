import matplotlib.pyplot as plt
import networkx as nx
from example_graphs import *
from math import ceil
import netgraph

for index, data in enumerate(all_graphs):
    graph, name, iterations = data
    if iterations is None:
        iterations = 50
    ax = plt.subplot(2, ceil(len(all_graphs)/2), index + 1)
    ax.title.set_text(name)
    pos = nx.drawing.spring_layout(graph, iterations=iterations)
    # netgraph.Graph(graph)
    nx.draw(graph, pos=pos)

plt.show()
