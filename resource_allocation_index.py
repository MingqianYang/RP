import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()

#Nodes

G.number_of_edges()


with open('Dataset/CollegeMsg.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        G.add_edge(inner_list[0], inner_list[1])


#G.add_edges_from(list_of_lists)
#print(G.number_of_nodes())
#print(G.number_of_edges())






#nx.draw(G)
#plt.show()

# exmaples https://www.programcreek.com/python/example/89543/networkx.degree_centrality
def CentralityMeasures(G):
	# Betweenness centrality
	bet_cen = nx.betweenness_centrality(G)
	# Closeness centrality
	clo_cen = nx.closeness_centrality(G)
	# Eigenvector centrality
	eig_cen = nx.eigenvector_centrality(G)
	# Degree centrality
	deg_cen = nx.degree_centrality(G)
	#print bet_cen, clo_cen, eig_cen
	print ("# Betweenness centrality:" + str(bet_cen))
	print ("# Closeness centrality:" + str(clo_cen))
	print ("# Eigenvector centrality:" + str(eig_cen))
	print ("# Degree centrality:" + str(deg_cen))


#main function
CentralityMeasures(G)

