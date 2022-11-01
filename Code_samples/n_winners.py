YEARS = ["2000\n","2001\n", "2019\n", "2020\n", "2021\n", "2022\n"]
with open("winners_list.txt","r") as infile:
    data = infile.readlines()
    list_of_dicts = []
    for i in range(len(data)):
        if data[i] in YEARS:
            new_dict = {}
            new_dict["year"] = data[i]
        else:
            data_list = data[i].split(",")
            winners_list = []
            for j in range(1, len(data_list)):
                winners_list.append(data_list[j])
            new_dict[data_list[0]] = winners_list
        if i < len(data) - 1:
            if data[i+1] in YEARS:
                list_of_dicts.append(new_dict)
    list_of_dicts.append(new_dict)
    for k in range(len(list_of_dicts)):
        print(list_of_dicts[k])