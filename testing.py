import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.karate_club_graph()

#Nodes
G.add_node(1)

G.number_of_edges()
list_of_lists = []

with open('Dataset/CollegeMsg.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        G.add_edge(inner_list[0], inner_list[1])
        #G.add_node(inner_list[0])
        #G.add_node(inner_list[1])
        
        #list_of_lists.append(inner_tuple)
        #print(inner_tuple)

#G.add_edges_from(list_of_lists)



#print(G.number_of_nodes())
#print(G.number_of_edges())






nx.draw(G)


plt.show()


