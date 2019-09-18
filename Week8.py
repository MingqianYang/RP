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
datasetpath = 'Dataset/CollegeMsg.txt'
result_output_path = 'Results/week8_results.txt'
generated_dataset = 'Dataset/generateddataset.txt'
percentage = 20

time_index = 0

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


def test_predictions(datasetPath, percentage, prediction_function):
    print("********************************")
    # Creating a graph
    Gr = nx.Graph()  # Remove redundant
    Ga = nx.Graph()
    Gb = nx.Graph()

    total_lines = 0
    currentIndex = 0
    bList = []
    filtered_list = []  # To store the new removed list

    # Remove redundant data
    with open(datasetPath) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split()]
            Gr.add_edge(inner_list[0], inner_list[1], weight=inner_list[time_index])

    with open(result_output_path, 'a+', encoding="utf-8") as f:
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

    print("选取无配对边的前： " + str(number_of_top_percent) + "个数据")

    cList = []
    topPercentList = mylist[0:number_of_top_percent]
    for item in topPercentList:
        cList.append((item[0], item[1]))

    dList = list(set(bList + cList))
    repeatedNumber = len(bList) + len(cList) - len(dList)

    print(prediction_function.__name__ + ": ")
    print("重复个数：" + str(repeatedNumber))
    print("%.3f" % (repeatedNumber / len(bList)))
    print("%.3f" % (repeatedNumber / len(topPercentList)))

    # Write results to file
    with open(result_output_path, 'a+', encoding="utf-8") as f:
        f.write("********************************\n")
        f.write(prediction_function.__name__ + "\n" )
        f.write("重复个数：{} \n" %(repeatedNumber))
        f.write("%.3f \n" % (repeatedNumber / len(bList)))
        f.write("%.3f \n" % (repeatedNumber / len(topPercentList)))
        f.flush()


def start_test():
    # print_filtered_dataset(datasetpath)
    # Remove the file first
    if os._exists(result_output_path):
        os.remove(result_output_path)

    for current_function in function_lists:
        with open(result_output_path, 'a+', encoding="utf-8") as f:
            f.write("*************** {} *****************\r\n".format(current_function.__name__))
            f.flush()

        for current_percentage in range(10, 100, 10):
            with open(result_output_path, 'a+', encoding="utf-8") as f:
                f.write("%%%%%%%%%%%% {} %%%%%%%%%%%%%%%%%%%%%%\r\n".format(current_percentage))
                f.flush()

            datasetfiles = os.listdir("Dataset/")
            for current_dataset in datasetfiles:
                if current_dataset == 'CollegeMsg.txt':
                    time_index = 2
                else:
                    time_index = 3

                current_dataset_name = "Dataset/" + current_dataset
                with open(result_output_path, 'a+', encoding="utf-8") as f:
                    f.write("^^^^^^^^^^^^^^^^^ {} ^^^^^^^^^^^^^^^^^\r\n ".format(current_dataset_name))
                    f.flush()


                test_predictions(current_dataset_name, current_percentage, current_function)




def main():
    start_test()

    with open(result_output_path, 'a+') as f:
        f.write("end")
        f.write("\r\n")
        f.flush()


if __name__ == "__main__":
    main()
