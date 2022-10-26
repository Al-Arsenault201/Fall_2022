# in-class coding for Wednesday, October 26

# we will import functions from the program dataEntry.py

from dataEntry import fill_attendance_data
from dataEntry import fill_roster

# this allows me to call those two functions in this program exactly as if I had copied
# and pasted them

if __name__ == "__main__":
    roster = fill_roster()
    print (roster)
    attendance_list = fill_attendance_data()
    print (attendance_list)


# alternate way
import dataEntry
import random
# if I import this way, I have to module_name.function_name
attendance_list = fill_attendance_data() #THIS would produce an error
#use
attendance_list = dataEntry.fill_attendance_data()   # this tells python which version of the function

