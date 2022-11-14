
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
#    print(new_d)
    return(new_d)   # note: last week's example omitted this


def read_a_file(filename):
    with open (filename, "r") as infile:
        first_header = infile.readline()
        second_header = infile.readline()
        data = infile.readlines()
#        print(data)
        for i in range(len(data)):
            data[i] = data[i].split(",")
#        print(data)
#for each student record, create the dictionary
#        d = create_dictionary(data[0])
        class_record = []
        for i in range(len(data)):
            d = create_dictionary(data[i])
            class_record.append(d)
        print(class_record)  # we can modify this to make the printing a little prettier


if __name__ == "__main__":
#    first_file = input("Enter the location of the first data file")
#    second_file = input("Enter the location of the second data file")
#    third_file = input("Enter the location of the third data file")

    first_file = "/users/alfredarsenault/PycharmProjects/Fall_2026.csv"
    first_list = read_a_file(first_file)