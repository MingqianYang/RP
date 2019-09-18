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


time_index = 0

# Remove the file first
if os._exists(result_output_path):
    os.remove(result_output_path)


# Start from the first cell below the headers.
manifest = 15

# Candidate tested functions
function_lists = [nx.resource_allocation_index,
                  nx.jaccard_coefficient,
                  nx.adamic_adar_index,
                  nx.preferential_attachment]




def test_predictions(datasetPath, percentage, prediction_function, worksheet, row, col):
    # Creating a graph
    Ga = nx.Graph()

    total_lines = 0
    currentIndex = 0
    bList = []
    filtered_list = []  # To store the new removed list

    # Loop the Dataset to calculate the total lines
    with open(datasetPath) as f:
        for line in f:
            total_lines = total_lines + 1


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
        print(current_function.__name__)
        worksheet = workbook.add_worksheet(current_function.__name__)
        row = 1
        col = 1

        for current_percentage in range(10, 100, 10):
            print('   %d '  %(current_percentage))
            # AUC y-axis
            worksheet.write(row, 0, current_percentage, bold)

            # precision y-axis
            worksheet.write(row, manifest, current_percentage, bold)

            col = 1
            datasetfiles = os.listdir("Dataset/")
            for current_dataset in datasetfiles:
                print("          {}" + (current_dataset))
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

        #break


    workbook.close()
def main():
    start_test()


    print("end")


if __name__ == "__main__":
    main()
