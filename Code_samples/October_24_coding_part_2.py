# an example of .csv files

with open ("class_example - Sheet1.csv","r") as f:
#    data = f.read()
#    print(data)
# read the first line of data and put it away
    headline = f.readline()
    data = f.read()   # read the REST of the file into a single string
    data_list = data.split('\n')
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(",") # change , to \t if it was tab-separated value

    #find all the baseball fans
    for i in range(len(data_list)):
        if data_list[i][5] == "Baseball":
            print(data_list[i][0], " is a baseball fan")

    #test
#    for i in range(len(data_list)):
#        print(data_list[i])
