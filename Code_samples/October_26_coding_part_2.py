# in class coding part 2

# let's create a dictionary of my dogs - current and former

dogs = {'doug':['beagle','bulldog'], 'bentley':['australian cattle dog','golden retriever','chow']
        'penny':'cocker spaniel', 'baron':'beagle'}

# make a dictionary of governors of states
# create an empty dictionary
governors = {}   # creates a new, empty dictionary
#add an element
governors['Maryland'] = "Hogan"
governors['Virginia'] = 'Youngkin'
governors['Louisiana'] = "Edwards"
governors['Nova Scotia'] = ['Trudeau', 'Harper']
governors['Ontario'] = "Hogan"

#changing a vlue
governors['Maryland'] = 'Moore'
print(governors['Virginia'])

# keys and values
governors.keys()  # creates an object that contains a list of all the keys
                        # in the dictionary
governors.values() # creates an object that contains a list of all the values
                        # in the dictionary

# the word in is useful here again

#check to see if I have a governor defined for 'Tennessee'
if 'Tennessee' in governors.keys():
        print(governors['Tennessee'])
else:
        print("I don't know who that governor is ")

# check to see if a value is in the dictionary
if 'Smith' in governors.values():
        print("Some governor is named Smith")
else:
        print("No, sorry")

#NOTE: this does not tell you the corresponding key

if 'Edwards' in governors.values():
        # what state is John Bel Edwards the Governor of?
        for state in governors.keys():
                if governors[state] == "Edwards":
                        print("He's the Governor of ", state)
