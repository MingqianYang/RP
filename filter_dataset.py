
import operator
import os


def test_predictions(datasetPath):
    l1 = []
    current_datasetPath = "Dataset/" + datasetPath
    # Populate the graph with half data
    with open(current_datasetPath) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split()]

            l1.append((inner_list[0], inner_list[1]))

    l2 = sorted(set(l1), key=l1.index)

    result_output_path = "NewDatasets/" + datasetPath
    outF = open(result_output_path, "w")
    for line in l2:
        # write line to output file
        outF.write("{} {}".format(line[0], line[1]))
        outF.write("\n")
    outF.close()


def main():

    datasetfiles = os.listdir("Dataset/")
    for current_dataset in datasetfiles:
        test_predictions(current_dataset)


if __name__ == "__main__":
    main()







