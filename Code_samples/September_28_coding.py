# in-class coding from Wednesday, September 28

# some illustrations of split
s = "The New Orleans Saints are having a disappointing year since Drew Brees retired"

#suppose we want to split this into words
# split on whitespace - blank spaces, tabs, newlines
l = s.split()  # leaving the parentheses blank means split on whitespace
print(l)

# split on any other character
le = s.split("e")
print(le)

#notice that the character you split on is thrown away

ling = s.split("ing")
print(ling)

v = "a"
la = s.split(v)
print(la)

s = "The New Orleans Saints are having a disappointing year since Drew Brees retired"
l = s.split()
print(l)

#the join command
new_string = "".join(l)
print(new_string)

# a true inverse
newer_string = " ".join(l)
print(newer_string)

#separate elements with tabs
tab_string = "\t".join(l)
print(tab_string)

# comma - separated value
comma_string = ",".join(l)
print(comma_string)

#edit a string
s = "The New Orleans Saints are having a disappointing year since Drew Brees retired"
l = s.split()
l[7] = "exciting"
happy_string = " ".join(l)
print(happy_string)

# while loops
# ask the user to enter the number of the current month - 1 for January, 12 for December, etc.
# loop until the user enters a valid month number

month = int(input("please enter the number of the current month, 1 through 12"))
while (month < 1) or (month > 12):
    print("That is not a valid month; please enter a number between 1 and 12 inclusive")
    month = int(input("please enter the number of the current month, 1 through 12"))
print ("The month entered was", month)

# can a while loop execute zero times? Sure.

# potential harm - can a while loop run forever? Sure
month = int(input("please enter the number of the current month, 1 through 12"))
while (month < 1) or (month > 12):
    print("That is not a valid month; please enter a number between 1 and 12 inclusive")
#    month = int(input("please enter the number of the current month, 1 through 12"))
print ("The month entered was", month)

# this ^ is an infinite loop

#enter six numbers using a for loop
numbers = []
for i in range(6):
    num = int(input("enter the next number"))
    numbers.append(num)

# the same code using a while loop
numbers = []
i = 0  # you must initialize the value of the iterator
while i < 6:
    num = int(input("enter the next number"))
    numbers.append(num)
    i += 1  # if you leave this statement out you will have an infinite loop


# priming read or priming assignment (typically, priming read)
# you have to get an initial value BEFORE you run the while loop

#here's a while loop that runs until the user types a specific value, "Q"
course = input("Enter the next course ID; enter 'Q' to stop")
while course.upper() != "Q":  #easier than writing while course != "Q" and course != "q":
    print(course)
    course = input("Enter the next course ID; enter 'Q' to stop")
print("done")

# this is a sentinel loop
# the value "Q" (or 'q') is the SENTINEL

