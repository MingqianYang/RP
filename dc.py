import networkx as nx
import matplotlib.pyplot as plt
import json

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
        with open('bet_cen_CollegeMsg.json', 'w') as f:
            json.dump(bet_cen, f)
            
	# Closeness centrality
	clo_cen = nx.closeness_centrality(G)
	with open('clo_cen_CollegeMsg.json', 'w') as f:
            json.dump(clo_cen, f)
            
	# Eigenvector centrality
	eig_cen = nx.eigenvector_centrality(G)
	with open('eig_cen_CollegeMsg.json', 'w') as f:
            json.dump(eig_cen, f)
            
	# Degree centrality
	deg_cen = nx.degree_centrality(G)
	with open('deg_cen_CollegeMsg.json', 'w') as f:
            json.dump(deg_cen, f)       
	#print bet_cen, clo_cen, eig_cen
	#print ("# Betweenness centrality:" + str(bet_cen))
	#print ("# Closeness centrality:" + str(clo_cen))
	#print ("# Eigenvector centrality:" + str(eig_cen))
	#print ("# Degree centrality:" + str(deg_cen))

#main function
CentralityMeasures(G)


