# in-class coding from Wednesday, September 21
states = ["Maine","New Hampshire","Vermont","Massachussetts","Rhode Island","Connecticut","New York"]
# add a state to the end of the list
states.append("New Jersey")
print(states)
#insert a state in a specific location - the second state in the list
states.insert(1, "Pennsylvania")
print(states)
# removing a list element by value
states.remove("Maine")
print(states)

# remove a list element by its index - in this case, index 3
states.pop(3)
print(states)

states = ["Maine","New Hampshire","Vermont","Massachussetts","Rhode Island","Connecticut","New York"]
print(states)
del states[1:3]  # this will delete elements 1 and 2 - New Hampshire and Vermont - and will LEAVE 3 - Mass.
print(states)

# notation - more proof that computer scientists are lazy
# if the length of a list is len(states), the last element in the list is always states[len(states) -1]
# you can abbreviate that as states[-1]
states = ["Maine","New Hampshire","Vermont","Massachussetts","Rhode Island","Connecticut","New York"]
print(states[-1])
states.append("Maryland")
print(states[-1])

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


#what if I wanted to take the first 10 states alphabetically?
first_states = states[0:10]
next_states = states[19:29]

#if you leave out the second number - the one after the colon - you get to the end of the list
final_states = states[19:]

# if you leave out the first number, you start from the beginning
first_ten = states[:10]

#if you leave out both numbers and just have a colon, you get the whole list
all_states = states[:]  #ensures you get the data at a NEW location in memory
                        # you can change the new value WITHOUT changing the old
the_states = states  # these two variables are at the SAME place in memory
                    # if you change one, you change them both whether you wanted to or not


# now the part about strings

phrase = "now is the time for all retrievers to support your school"
print(len(phrase))
print(phrase[0]) # this will print the first character in the string

# string slicing works like list slicing
first_ten_chars = phrase[0:10]
print(first_ten_chars)

# how a list is not a string
#for a list
states[45] = "East Virginia"
new_phrase = "UMCC rocks"

#try to change new_phrase[2] to a "B"
new_phrase[2] = "B"

#start over
new_phrase = "UMBC rocks"
correct_phrase = new_phrase[0:2]+"B"+new_phrase[3:]
print(correct_phrase)

#back to our original phrase
phrase = "now is the time for all retrievers to support your school"
#suppose you want to break down this phrase into its component words
# python provides you the split function that does just that
word_list = phrase.split()

#strip function gets rid of extra whitespace at beginning and end of strings
data = input("enter a string")
print(data,"is what the user typed")
#data = data.strip()
print(data, "is what the user typed after it's been stripped")
#did the user type why not?
if data == 'why not':
    print("it matched")
else:
    print("it didn't")