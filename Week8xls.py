import networkx as nx
import xlsxwriter
import operator
import os




time_index = 0
dataset_percentage = 0



# Start from the first cell below the headers.
manifest = 15

# Candidate tested functions
function_lists = [nx.resource_allocation_index,
                  nx.jaccard_coefficient,
                  nx.adamic_adar_index,
                  nx.preferential_attachment]

precentage_conatainer = [0.1, 0.3, 0.5, 0.7, 0.9]

def test_predictions(datasetPath, threshold, percentage, prediction_function, worksheet, row, col):
    # Creating a graph
    Ga = nx.Graph()

    total_lines = 0
    currentIndex = 0
    bList = []

    # Loop the Dataset to calculate the total lines
    with open(datasetPath) as f:
        for line in f:
            total_lines = total_lines + 1


    # Populate the graph with half data
    with open(datasetPath) as f:

        for line in f:
            currentIndex += 1
            inner_list = [int(elt.strip()) for elt in line.split()]

            if currentIndex <= total_lines * percentage:
                Ga.add_edge(inner_list[0], inner_list[1])
            else:
                if currentIndex >= total_lines:
                    break
                bList.append((inner_list[0], inner_list[1]))


    no_edge_pairs = nx.non_edges(Ga)

    preds = prediction_function(Ga, list(no_edge_pairs))
    mylist = (list(preds))
    mylist.sort(key=operator.itemgetter(2), reverse=True)

    number_of_top_percent = int(threshold * (len(mylist) / 100))

    cList = []
    topPercentList = mylist[0:number_of_top_percent]
    for item in topPercentList:
        cList.append((item[0], item[1]))

    dList = list(set(bList + cList))
    repeatedNumber = len(bList) + len(cList) - len(dList)

    worksheet.write(row, col, round(repeatedNumber / len(bList),3) )
    worksheet.write(row, col + manifest, round(repeatedNumber / len(topPercentList), 3) )



def start_test():

    for current_dataset_percentage in precentage_conatainer:
        print('%f ' % (current_dataset_percentage))

        result_output_path = "Results/results" + str(current_dataset_percentage*10) + ".xlsx"
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(result_output_path)

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        for current_function in function_lists:
            print(current_function.__name__)
            worksheet = workbook.add_worksheet(current_function.__name__)
            row = 1
            col = 1

            for current_threshold in range(10, 91, 20):
                print('   %d '  %(current_threshold))
                # AUC y-axis
                worksheet.write(row, 0, current_threshold, bold)
                worksheet.write(row+1, 0, "Average", bold)

                # precision y-axis
                worksheet.write(row, manifest, current_threshold, bold)

                col = 1
                datasetfiles = os.listdir("NewDatasets/")
                for current_dataset in datasetfiles:
                    print("          {}" + (current_dataset))
                    # AUC x-axis
                    worksheet.write(0, col, current_dataset, bold)

                    # precision x-axis
                    worksheet.write(0, col + manifest, current_dataset, bold)

                    current_dataset_name = "NewDatasets/" + current_dataset


                    test_predictions(current_dataset_name, current_threshold, current_dataset_percentage, current_function, worksheet, row, col)

                    col += 1

                row += 1
            # average
            worksheet.write(row + 1, col, '=AVERAGE(B2:B7)')


        workbook.close()

def main():
    start_test()

    print("end")


if __name__ == "__main__":
    main()
