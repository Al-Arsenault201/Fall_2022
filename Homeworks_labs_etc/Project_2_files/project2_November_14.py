
def create_dictionary(student_record):
    new_d = {}
    new_d["last name"]=student_record[0]
    new_d["first name"] = student_record[1]
    new_d["student ID"] = student_record[2]
    new_d["P1"] = int(student_record[3])
    new_d["P2"] = int(student_record[4])
    new_d["P3"] = int(student_record[5])

    #insert more key/value pairs for the test grades
    #remember to convert the strings to integers

    return(new_d)   # note: last week's example omitted this


def read_a_file(filename):
    with open (filename, "r") as infile:
        first_header = infile.readline()
        second_header = infile.readline()
        data = infile.readlines()
        print(data)
        for i in range(len(data)):
            data[i] = data[i].split(",")

        class_record = []
        for i in range(len(data)):
            d = create_dictionary(data[i])
            class_record.append(d)
#        print(class_record)  # we can modify this to make the printing a little prettier
        print_a_list_of_dictionaries(class_record)


def print_a_list_of_dictionaries(class_roster):
    # a helper function we've written to make it easier to read our
    # printouts and ensure we have the right answer
    for i in range(len(class_roster)):
        print ("student ", i)
        for key in class_roster[i].keys():
            print (key, ":", class_roster[i][key])

def get_files_to_read():
    """

    :return: a list of the paths to the files to be read
    """
    list_of_filenames = []
    num_files = int(input("How many data files are we reading?"))
    for i in range(num_files):
        filename = input("Enter the path to the next file to read")
        list_of_filenames.append(filename)
    return list_of_filenames

def add_new_values(class_list):
    """

    :param class_list: the list to which you're going to add new values
    :return: updated list with new values inserted
    """
    # add a new key value pair for project total
    # key: "Project_total"
    # value: sum of the three values associated with the project scores
    for i in range(len(class_list)):
        project_total = class_list[i]["P1"] + class_list[i]["P2"] + class_list[i]["P3"]
        class_list[i]["Project_total"] = project_total
        #the student adds code to the overall total
        # take line 64 and add "T1" score + "T2" score + "T3" score
        #student then calculates letter grade:
        # if total_score >= 576:
        #   letter_grade = "A"
        # elif total_score>= 512:
        #   letter_grade = "B"
        #....
    return class_list


if __name__ == "__main__":

    """
    first_file = "/users/alfredarsenault/PycharmProjects/Fall_2026.csv"
    first_list = read_a_file(first_file)
"""

    f_list = get_files_to_read()
    first_file = f_list[0]
    second_file = f_list[1]
    third_file = f_list[2]
    print (third_file)
#    for i in range(len(f_list)):
#        read_a_file(f_list[i])
    first_list = read_a_file(first_file)
    second_list = read_a_file(second_file)
    third_list = read_a_file(third_file)

#    print_a_list_of_dictionaries(third_list)
    # call add_new_values for each of the three files - That's step 2
