import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()


with open('Dataset/CollegeMsg.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        G.add_edge(inner_list[0], inner_list[1])



preds = nx.resource_allocation_index(G.to_undirected(), [(1, 2), (3, 4)])
for u, v, p in preds:
    print('(%d, %d) -> %.8f' % (u, v, p))
