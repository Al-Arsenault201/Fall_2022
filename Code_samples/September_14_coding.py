# in-class coding from Wednesday, September 14

#simplest case: one action.
# do something, or do nothing

# ask the user for her grade
grade = int(input("Please enter your grade on the test"))
if grade >= 90:
    print("Excellent work!!")
    print("You know we expect nothing less at UMBC")
    print("Keep it up")
print("The conditional is over")

# more complex case: do one thing, or do another
grade = int(input("Please enter your grade on the test"))
if grade >= 90:
    print("Excellent work")
    print("Keep it up")
else: # what we're going to do if that Boolean evaluated to false
    print("Okay, you got a B; that's not terrible")
    print("but please try to meet UMBC standards in the future")
print("The conditional is over")

# else if
#elif
grade = int(input("Please enter your grade on the test"))
if grade >= 90:
    print("Excellent work")
    print("Keep it up")
elif grade >= 80 and grade < 90:  # doesn't hurt; but not needed
    print("Okay, you got a B; that's not terrible")
    print("but please try to meet UMBC standards in the future")
elif grade >= 70:
    print ("Are you kidding me with this C nonsense?")
elif grade >= 60:
    print ("You are like a submarine - below C level a lot")
else:
    print("I have no words")

print("We're done")

y = 5
#y = y + 2
y += 2 # means exactly the same as y = y + 2
y *= 2 # means y = y * 2
y -= 2 # means y = y -2 NOT y = 2 - y
y /= 2 # means y = y/2  NOT y = 2/y

x = 5
y = 3 + 3
if x == y:
    print("5 is equal to y")
else:
    print("it's not")