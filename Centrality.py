import networkx as nx
import matplotlib.pyplot as plt
import json
import xlsxwriter


# Creating a graph
G = nx.Graph()


# Populate the graph with data extracted from database
with open('Dataset/CollegeMsg') as f:
    for line in f:
        inner_list = [int(elt.strip()) for elt in line.split()]
        G.add_edge(inner_list[0], inner_list[1])


# exmaples https://www.programcreek.com/python/example/89543/networkx.degree_centrality
def CentralityMeasures(G):
    row = 0
    col = 0

    # Degree centrality
    deg_cen = nx.degree_centrality(G)
    with open('Results/deg_cen_CollegeMsg.json', 'w') as f:
        json.dump(deg_cen, f)
    print("deg_cen_CollegeMsg.json finished ")

    # Write to excelfile
    workbook = xlsxwriter.Workbook('Results/deg_cen_CollegeMsg.xlsx')
    worksheet = workbook.add_worksheet()
    for key, value in deg_cen.items():
        row += 1
        worksheet.write(row, col, key)
        worksheet.write(row, col + 1, value)
    workbook.close()

    # Closeness centrality
    clo_cen = nx.closeness_centrality(G)
    with open('Results/clo_cen_CollegeMsg.json', 'w') as f:
        json.dump(clo_cen, f)
    print("clo_cen_CollegeMsg.json finished ")

    # Betweenness centrality
    bet_cen = nx.betweenness_centrality(G)
    with open('Results/bet_cen_CollegeMsg.json', 'w') as f:
        json.dump(bet_cen, f)
    print("bet_cen_CollegeMsg.json finished ")
            
'''    
    # Eigenvector centrality
    eig_cen = nx.eigenvector_centrality(G)
    with open('eig_cen_CollegeMsg.json', 'w') as f:
        json.dump(eig_cen, f)
    print("eig_cen_CollegeMsg.json finished ")         
'''


# main function
CentralityMeasures(G)

