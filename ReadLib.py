from xlrd import open_workbook
from ClfUtils import initialize_list_of_lists
from Dataset import Dataset

def read_data_file(filename: str):
    """Reads data from given file

    :param filename: Name of the file to read
    :return:
    """
    if filename.endswith(".dat") or filename.endswith(".csv"):
        X, y = read_sv_file(filename, ",")
    elif filename.endswith(".tsv"):
        X, y = read_sv_file(filename, '\t')
    elif filename.endswith(".scsv"):
        X, y = read_sv_file(filename, ';')
    else:
        X, y = read_excel_file(classifier_data)
    X0, X1 = make_selection(X, y, classifier_data)
    print('Ratio (0:1): {}:{}'.format(len(X0), len(X1)))
    X0, X1 = sort_attributes(X0), sort_attributes(X1)
    if is_validation_hard:
        assert_distribution(X0, X1, classifier_data)
    else:
        assert_distribution_simplified(X0, X1, classifier_data)
    X, y = compose_sorted_parts(X0, X1)
    return X, y


def read_sv_file(filename: str, separator: str = ','):
    """Reads data from tab separated value files
    :param filename: Name of the file
    :param separator: str
    :return: X, y: [], []
    """
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    X, y = [], []
    for line in lines:
        if line.startswith("@"):
            continue
        line_as_array = line.replace("\n", "", 1).split(separator)
        row = []
        for i in range(len(line_as_array) - 1):
            row.append(float(line_as_array[i]))
        X.append(row)
        y.append(int(float(line_as_array[-1])))
    return X, y


def read_2018_07_02(filename: str = "Filtr_2_07_2018.xlsx", p: int = 1):
    file = open_workbook(filename)
    sheet = file.sheet_by_index(0)
    line_number = 0
    X, y = initialize_list_of_lists(10), initialize_list_of_lists(10)
    X_test, y_test = initialize_list_of_lists(10), initialize_list_of_lists(10)
    while line_number < sheet.nrows - 1:
        line_number += 1
        line = sheet.row(line_number)
        if int(line[0].value) != p:
            continue
        row = []
        for i in range(1, 9):
            row.append(float(line[i].value))
        number_of_set = int(line[10].value) - 1
        if int(line[11].value) == 0:
            X[number_of_set].append(row)
            y[number_of_set].append(int(float(line[9].value)))
        else:
            X_test[number_of_set].append(row)
            y_test[number_of_set].append(int(float(line[9].value)))
    return Dataset(X, y, X, y, X_test, y_test)

