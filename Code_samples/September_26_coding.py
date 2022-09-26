#in-class coding from Monday, September 26

grocery_list = ["milk","eggs","bread","grapes","yogurt","bagels","toothpaste"]

# walk through the list and print out each item, one per line
#for item in grocery_list:
#    print(item)
#    print(item)

for item in grocery_list:
    if item[0] == "g":
        print(item)
    else:
        print("nope")


states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# suppose that I want to print out every state that begins with "M"
# for each loop: take each of the list, one at time.
# decide if it starts with "M". If so, print it; if not, move on
for state in states:
    if state[0] == "M":
        print(state)

# fancy up the output:
print ("The states that begin with M are: ", end=", ")
for state in states:
    if state[0] == "M":
        print(state, end=",")

#print out every state that ends in a vowel
VOWELS = ['a','e','i','o','u','y']
print("The states the end with a vowel are: ")
for state in states:
    if state[-1] in VOWELS:
        print(state)

vowel_states = []
for state in states:
    if state[-1] in VOWELS:
        vowel_states.append(state)

#a for i loop
for i in range(0,10,1):
    print(i)
# do not execute loop when i >= 10

# bigger hop count
for i in range(0,10,3):
    print(i)

#use of a negative hop count
for i in range(0,10, -1):
    print(i)

#you can go down
for i in range(10, 0, -1):
    print(i)

word = "supercalifragilisticexpialidocious"
new_list = []
for i in range(len(word)-1,-1,-1):  # this lets us take the characters in reverse order
    new_list.append(word[i])
print(new_list)
new_word = "".join(new_list)
print(new_word)

#not all three parameters in the range statement have to be there
# if there are only two - the hop count defaults to 1
# if there's only one - the starting value defaults to 0
for i in range(10):  #identical to range(0,10,1) because of the defaults
    print(i)

for i in range(5,15):  # start with 5; end at 15; hop count is 1
    print(i)

#can you use something other than i:
for j in range(5,15):
    print(j)

#what happens if you change the value in the loop:
for i in range(0,10,1):
    if i%2 == 0:  # if i is even
        i += 2
    print(i)

# here's a list of your lab grades
grades = [8,8,6,10,8,0,2]
#now I suddenly discover there was an error with an assignment and I want to increase each grade by 2

#for each loop:
for grade in grades:
    grade += 2
print(grades)
# you cannot modify the original list variable with a for each loop

for i in range(len(grades)):
    grades[i] += 2
print(grades)

# if you want to modify the original list inside the loop, you must use for i

answer = input("What's today's word")
for i in range(6): #you get 6 guesses
    response = []
    guess = input("What's your next guess")
    for i in range(len(guess)):  #could just be 5
        if not guess[i] in answer:
            response.append( "b")
        elif guess[i] == answer[i]:
            response.append("g")
        else:
            response.append("y")
    print(response)
