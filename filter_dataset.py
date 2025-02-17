import operator
import os


def test_predictions(datasetPath):
    l1 = []
    current_datasetPath = "Dataset/" + datasetPath
    # Populate the graph with half data
    with open(current_datasetPath) as f:
        for line in f:
            inner_list = [(elt.strip()) for elt in line.split()]

            if datasetPath == "CollegeMsg" or datasetPath == "EEC" :
                l1.append((inner_list[0], inner_list[1], inner_list[2]))
            else:
                l1.append((inner_list[0], inner_list[1], inner_list[3]))

    l2 = sorted(set(l1), key=l1.index)

    # loop l1

    result_output_path = "NewDatasetsWithTime/" + datasetPath
    outF = open(result_output_path, "w")
    for line in l2:
        # write line to output file
        outF.write("{} {} {}".format(line[0], line[1], line[2]))
        outF.write("\n")
    outF.close()


def main():
    datasetfiles = os.listdir("Dataset/")
    for current_dataset in datasetfiles:
        test_predictions(current_dataset)


if __name__ == "__main__":
    main()
