import networkx as nx
import matplotlib.pyplot as plt
import json
import xlsxwriter


# Creating a graph
G = nx.Graph()


# Populate the graph with data extracted from database
with open('Dataset/CollegeMsg.txt') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split(' ')]
        G.add_edge(inner_list[0], inner_list[1])




def SimilarityMeasures(G):

    # resource_allocation_index
    preds = nx.resource_allocation_index(G, [(1, 2), (3, 4), (1, 4), (5, 6), (3, 5)])
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))

    print('****************************')


    # Common neighours
    print(sorted(nx.common_neighbors(G, 1, 2)))
    print('****************************')

    # jaccard coefficient
    preds = nx.jaccard_coefficient(G, [(1, 2), (3, 4), (1, 4), (5, 6), (3, 5)])
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))

    print('****************************')

    # AdamicAdar
    preds = nx.adamic_adar_index(G, [(1, 2), (3, 4), (1, 4), (5, 6), (3, 5)])
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))

    print('****************************')

    # Preferential Attachment (PA),
    preds = nx.preferential_attachment(G, [(1, 2), (3, 4), (1, 4), (5, 6), (3, 5)])
    for u, v, p in preds:
        print('(%d, %d) -> %.8f' % (u, v, p))

    print('****************************')

SimilarityMeasures(G)