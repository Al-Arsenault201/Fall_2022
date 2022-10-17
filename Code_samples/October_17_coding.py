#in-class coding for Monday, October 17

medal_table =[
    [1,7,12,7,26],  #this is a row
    [2,5,0,0,5],    # this is a row
    [3,4,4,2,10],   # this is a row
    [4,4,2,3,9],
    [5,4,1,4,9]
]

# a 2-dimensional list - it is a list whose elements are  themselves lists
print(medal_table)

# rows and columns
#Python uses row-major order

print(medal_table[1])

for i in range(len(medal_table)):
    print("row ",i, " is ", medal_table[i])

# a specific element: how many gold medals did the US win?
print("The US won ", medal_table[0][1], " gold medals ")

#very common mistake: medal_table[0,1]

# the row number ALWAYS comes first!!
medal_table [1][2]

len(medal_table)  # this is the number of ROWS!

# to deal with a column, you have to write a loop that deals with one row at a time

#what are the total number of medals that these first 5 countries
total_medals = 0
for i in range(len(medal_table)):   # this guarantees I hit every row in the 2-D list
    total_medals += medal_table[i][4]
print("These 5 countries won ", total_medals, " medals")

#medal_table[i] is a row
#append a row:
medal_table.append([6,3,3,3, 9])
#medal_table.insert(len(medal_table),[6,3,3,3,9])
print(medal_table)

country_names = ["USA","Italy","Kenya","Poland","Jamaica","Ethiopia"]
# to add a column, we have to write a loop

for i in range(len(medal_table)):  # hits every row
    medal_table[i].insert(1, country_names[i])
    print(medal_table[i])

RANK = 0
COUNTRY = 1
CONTINENT = 2
GOLDS = 3
SILVERS = 4
BRONZES = 5
TOTAL = 6

for i in range(len(medal_table)):
    print(medal_table[i][COUNTRY], medal_table[i][GOLDS])


#add a column that identifies the continent
continents = ["NA","EU","AF","EU","NA","AF"]
for i in range(len(medal_table)):
    medal_table[i].insert(2,continents[i])
    print(medal_table[i])


# we don't need every row to be the same length

grades = [
    [10, 10, 9],
    [10, 10],
    [10, 5,5, 10],
    [10, 8, 6]
]

# we do not require every row to be the same length
# BUT: if you have rows of different lenghths, you have to be careful with your subscripts

#if every row is the same length: pick one row and apply it everywhere.

#print all the values in the 2D list one at a time.
for i in range(len(medal_table)):
    for j in range(len(medal_table[1])):
        print(medal_table[i][j])


# create a 2D list with the first 50 squares (starting at 0)
# put it in a 2D list with 5 rows and 10 columns

ROWS = 5
COLUMNS = 10
square_table = []  # this is how you initialize a 2D list
for i in range(ROWS):
    for j in range(COLUMNS):
        new_row = []
        new_row.append((i*COLUMNS + j)**2)
#        square_table[i][j] = i * COLUMNS + j
    square_table.append(new_row)

print(square_table)
