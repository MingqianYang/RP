import networkx as nx
import matplotlib.pyplot as plt
import json
import xlsxwriter
import operator

datasetpath = 'Dataset/CollegeMsg.txt'

def test(datasetPath):
    # Creating a graph
    Ga = nx.Graph()
    Gb = nx.Graph()

    index = 0
    currentIndex = 0
    bList = []


    # Loop the Dataset to calculate the total lines
    with open(datasetPath) as f:
        for line in f:
            index = index + 1
    print("total lines is :" + str(index))

    # Populate the graph with half data
    with open(datasetPath) as f:

        for line in f:
            currentIndex += 1
            inner_list = [int(elt.strip()) for elt in line.split(' ')]

            if currentIndex <= index/2:
                Ga.add_edge(inner_list[0], inner_list[1])
            else:
                Gb.add_edge(inner_list[0], inner_list[1])
                bList.append((inner_list[0], inner_list[1]))

    no_edge_pairs = nx.non_edges(Ga)

    # resource_allocation_index jaccard_coefficient  adamic_adar_index
    preds = nx.adamic_adar_index(Ga, list(no_edge_pairs))
    mylist = (list(preds))
    mylist.sort(key = operator.itemgetter(2), reverse = True)

    number_0f_top_percent = int(len(mylist) / 25)
    print("选取前： " + str(number_0f_top_percent) + "个数据")

    cList = []
    topPercentList = mylist[0:number_0f_top_percent]
    for item in topPercentList:
        cList.append((item[0], item[1]))

    dList = list(set(bList + cList))
    repeatedNumber = len(bList) + len(cList) - len(dList)


    print("重复个数：" + str(repeatedNumber))
    print(str(repeatedNumber / len(bList)))
    print(str(repeatedNumber / len(topPercentList)))



test(datasetpath)

''' 
18865
%20 = %4

0.6432916638812755
0.6124033474400993

0.6330302827729126
0.6026346771884049

0.642222073668026
0.611385114710281

row = 0
col = 0
# 把不存在的配对写到文件中
# Write to excelfile
workbook = xlsxwriter.Workbook('Results/noPairs_CollegeMsg.xlsx')
worksheet = workbook.add_worksheet()
for s in list(noEdgePairs):
    mytuple = tuple(s)
    row += 1

    worksheet.write(row, col, mytuple[0])
    worksheet.write(row, col + 1, mytuple[1])

    preds = nx.resource_allocation_index(G, [(mytuple[0], mytuple[1])])
    for u, v, p in preds:
        #print('(%d, %d) -> %.8f' % (u, v, p))
        worksheet.write(row, col + 2, p)
workbook.close()

'''





