import networkx as nx
import matplotlib.pyplot as plt
import json
import xlsxwriter
import operator
import os

# print(__file__)

# facebook-wosn-links out.contact CollegeMsg.txt
# out.sociopatterns-hypertext.txt
# out.sociopatterns-infectious.txt
#datasetpath = 'Dataset/CollegeMsg.txt'
result_output_path = 'Results/myresults.xlsx'
generated_dataset = 'Dataset/generateddataset.txt'
new_database_info = 'Results/mydatabase.txt'

time_index = 0

# Remove the file first
if os._exists(result_output_path):
    os.remove(result_output_path)

if os._exists(new_database_info):
    os.remove(new_database_info)

# Start from the first cell below the headers.
manifest = 15

# Candidate tested functions
function_lists = [nx.resource_allocation_index,
                  nx.jaccard_coefficient,
                  nx.adamic_adar_index,
                  nx.preferential_attachment]


def print_filtered_dataset(datasetPath):
    # Creating a graph
    Gr = nx.Graph()  # Remove redundant
    filtered_list = []  # To store the new removed list
    # Remove redundant data
    with open(datasetPath) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split()]
            Gr.add_edge(inner_list[0], inner_list[1], weight=inner_list[time_index])

    total_lines = len(Gr.edges())
    tempstring_list = list(nx.generate_edgelist(Gr, data=['weight']))

    for item in tempstring_list:
        inner_list = [int(elt.strip()) for elt in item.split()]
        filtered_list.append((inner_list[0], inner_list[1], inner_list[2]))

    # Order filtered_list with weight vlue
    filtered_list.sort(key=lambda elem: elem[2])
    with open(generated_dataset, 'w') as f:
        for item in filtered_list:
            f.write(str(item[0]) + " " + str(item[1]) + " " + str(item[2]) + "\n")


def test_predictions(datasetPath, percentage, prediction_function, worksheet, row, col):
    print("********************************")
    # Creating a graph
    Gr = nx.Graph()  # Remove redundant
    Ga = nx.Graph()

    total_lines = 0
    currentIndex = 0
    bList = []
    filtered_list = []  # To store the new removed list

    # Remove redundant data
    with open(datasetPath) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split()]
            Gr.add_edge(inner_list[0], inner_list[1], weight=inner_list[time_index])

    with open(generated_dataset, 'a+', encoding="utf-8") as f:
        f.write("新生成的dataset，总边长为：{} \r\n".format(len(Gr.edges())))
        f.write("新生成的dataset，点数为： {} \r\n".format(len(Gr.nodes())))
        f.flush()

    total_lines = len(Gr.edges())
    tempstring_list = list(nx.generate_edgelist(Gr, data=['weight']))

    for item in tempstring_list:
        inner_list = [int(elt.strip()) for elt in item.split()]
        filtered_list.append((inner_list[0], inner_list[1], inner_list[2]))

    # Order filtered_list with weight vlue
    filtered_list.sort(key=lambda elem: elem[2])

    for item in filtered_list:
        currentIndex += 1

        # put half of data into graph a
        if currentIndex <= total_lines / 2:
            Ga.add_edge(item[0], item[1])
        else:  # put half of data into list  b
            if currentIndex >= total_lines:
                break
            bList.append((item[0], item[1]))

    no_edge_pairs = nx.non_edges(Ga)

    preds = prediction_function(Ga, list(no_edge_pairs))
    mylist = (list(preds))
    mylist.sort(key=operator.itemgetter(2), reverse=True)

    number_of_top_percent = int(percentage * (len(mylist) / 100))

    cList = []
    topPercentList = mylist[0:number_of_top_percent]
    for item in topPercentList:
        cList.append((item[0], item[1]))

    dList = list(set(bList + cList))
    repeatedNumber = len(bList) + len(cList) - len(dList)

    worksheet.write(row, col, round(repeatedNumber / len(bList),3) )
    worksheet.write(row, col + manifest, round(repeatedNumber / len(topPercentList), 3) )



def start_test():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(result_output_path)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    for current_function in function_lists:

        worksheet = workbook.add_worksheet(current_function.__name__)
        row = 1
        col = 1

        for current_percentage in range(10, 100, 10):
            # AUC y-axis
            worksheet.write(row, 0, current_percentage, bold)

            # precision y-axis
            worksheet.write(row, manifest, current_percentage, bold)

            col = 1
            datasetfiles = os.listdir("Dataset/")
            for current_dataset in datasetfiles:
                # AUC x-axis
                worksheet.write(0, col, current_dataset, bold)
                # precision x-axis
                worksheet.write(0, col + manifest, current_dataset, bold)

                if current_dataset == 'CollegeMsg':
                    time_index = 2
                else:
                    time_index = 3

                current_dataset_name = "Dataset/" + current_dataset
                test_predictions(current_dataset_name, current_percentage, current_function, worksheet, row, col)

                col += 1

            row += 1


    workbook.close()


def main():
    start_test()

    print("end")


if __name__ == "__main__":
    main()
