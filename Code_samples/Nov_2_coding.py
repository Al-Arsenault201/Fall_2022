# in-class coding for Wednesday, November 2

from statistics import median

def calc_median_steps (dataset):
    steps_per_day = []
    for i in range(len(dataset)):
        steps_per_day.append(dataset[i][2])
    print("The median number of steps is ", end = "  ")
    print(median(steps_per_day))


def get_data_file(input_file):
    with open (input_file,"r") as infile:
        header_line = infile.readline()  # reads the line of column headers and puts it someplace I can later use it
        #now read the rest of the file
        data = infile.read()  #data is a single string
        data_list = data.split("\n")
#        print (data_list)
        for i in range(len(data_list)):
            data_list[i] = data_list[i].split(",")   # if this was a .tsv instead of a .csv, we would split on "\t"
#            print(data_list[i])
        revised_data_list = format_data(data_list)
#        print(revised_data_list)
    return revised_data_list

def format_data(in_list):
    CONVERT_TO_INTS = [1,2,4,5]
    for i in range(len(in_list)):
        for j in range(len(in_list[i])):
            if j in CONVERT_TO_INTS:
                in_list[i][j] = int(in_list[i][j])
            if j == 3:
                in_list[i][j] = float(in_list[i][j])
    return in_list

def total_calories(dataset):
    #sum the entries in column 5 of each row
    sum = 0
    for i in range(len(dataset)):
        sum += dataset[i][5]
    print ("The total number of calories burned is ", sum)

if __name__ == "__main__":
    input_file = input("Enter the name of the data file")
    my_data = get_data_file(input_file)
    print ("What do you want to do?")
    print ("Enter q to quit; 1 to calculate the mean number of minutes")
    print ("2 to calculate the median number of steps, 3 to calculate the total number of calories")
    choice = input("Enter your choice")
    if choice != "q":
        choice = int(choice)
    #now call the appropriate function
    if choice == 3:
        total_calories(my_data)
    if choice == 2:
        calc_median_steps(my_data)