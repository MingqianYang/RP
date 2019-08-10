import networkx as nx
import matplotlib.pyplot as plt
import json

# Creating a graph
G = nx.Graph()
G = nx.complete_graph(100)



        



#G.add_edges_from(list_of_lists)
#print(G.number_of_nodes())
#print(G.number_of_edges())

H=G.to_undirected()
preds = nx.jaccard_coefficient(G.to_undirected(), [(0, 1), (3, 4)])
for u, v, p in preds:
    print('(%d, %d) -> %.8f' % (u, v, p))



with open('Dataset/CollegeMsg.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        #G.add_edge(inner_list[0], inner_list[1])
        G.add_node(inner_list[0])
        G.add_node(inner_list[1])


    
