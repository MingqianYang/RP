import networkx as nx
import matplotlib.pyplot as plt
import json
import xlsxwriter
import operator
import os

# facebook-wosn-links CollegeMsg
datasetpath = 'Dataset/CollegeMsg.txt'
result_output_path = 'Results/results.txt'

percentage = 20


# Candidate tested functions
function_lists = [nx.resource_allocation_index,
                  nx.jaccard_coefficient,
                  nx.adamic_adar_index,
                  nx.preferential_attachment]

def test_predictions(datasetPath, percentage, prediction_function):
    # Creating a graph
    Ga = nx.Graph()

    total_lines = 0
    currentIndex = 0
    bList = []

    # Loop the Dataset to calculate the total lines
    with open(datasetPath) as f:
        for line in f:
            total_lines = total_lines + 1
    print("total lines is :" + str(total_lines))

    # Populate the graph with half data
    with open(datasetPath) as f:

        for line in f:
            currentIndex += 1
            inner_list = [int(elt.strip()) for elt in line.split()]

            if currentIndex <= total_lines/2:
                Ga.add_edge(inner_list[0], inner_list[1])
            else:
                if currentIndex >= total_lines:
                    break
                bList.append((inner_list[0], inner_list[1]))

    no_edge_pairs = nx.non_edges(Ga)

    preds = prediction_function(Ga, list(no_edge_pairs))
    mylist = (list(preds))
    mylist.sort(key = operator.itemgetter(2), reverse = True)

    number_of_top_percent = int(percentage * (len(mylist) / 100))
    print("选取前： " + str(number_of_top_percent) + "个数据")

    cList = []
    topPercentList = mylist[0:number_of_top_percent]
    for item in topPercentList:
        cList.append((item[0], item[1]))

    dList = list(set(bList + cList))
    repeatedNumber = len(bList) + len(cList) - len(dList)

    print("********************************")
    print(prediction_function.__name__ + ": ")
    print("重复个数：" + str(repeatedNumber))
    print(str(repeatedNumber / len(bList)))
    print(str(repeatedNumber / len(topPercentList)))

    # Write results to file
    with open(result_output_path, 'a+') as f:
        f.write("********************************\r\n" )
        f.write(prediction_function.__name__ + ": \r\n")
        f.write("重复个数：" + str(repeatedNumber) +"\r\n")
        f.write(str(repeatedNumber / len(bList)) +"\r\n")
        f.write(str(repeatedNumber / len(topPercentList)) +"\r\n")


def start_test ():
    # Remove the file first
    if  os._exists(result_output_path):
        os.remove(result_output_path)

    for item in function_lists:
        test_predictions(datasetpath, percentage, item)





def main():
    start_test()


if __name__ == "__main__":
    main()

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





