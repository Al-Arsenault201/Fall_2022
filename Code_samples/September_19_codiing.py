# in-class coding from Monday, September 19
"""
x ="Hello"+"world"

print("Hello","world",34)  # the comman inserts one blank space between elements

#if you want to print elements with no blank spaces - use string concatenation
print("Hello"+"world")

# convert to all uppercase
x = input("type a string")
y = x.upper()
print(y)

# convert to all lowercase
x = input("type a string")
y = x.lower()
print(y)
"""

# stuff about lists

# create a new variable that is an empty list
grocery_list = []    # empty list; holds zero elements
print ("My list is", grocery_list)

#add an element to the list - a new value
#add to the end of the list - append
grocery_list.append("Apples")
grocery_list.append("Oranges")
#grocery_list.append(42)
grocery_list.append("Eggs")
#grocery_list.append("Milk","Bread")   - error because you can only append one item at a time
print ("My list is", grocery_list)

#check to see if a value is in a list
if "Eggs" in grocery_list:
    print("You already have eggs on the list")
else:
    print("you forgot 'em")

# what if I don't want to put an item last? I want to put a new item first.
print(grocery_list[0])

grocery_list.insert(0,"Bread")
print(grocery_list)

# build a list that is NOT empty to start
g_list = ["apples","peaches","pumpkins","pie","ice cream","rice","beans"]
print(g_list)


g_list = ["apples","peaches","pumpkins","pie","ice cream","rice","beans"]
g_list.remove("pumpkins")  #remove this element by its value
print(g_list)

g_list.pop(3)  # removes the item at that index - it will print out the name of the item it deletes

#what happens if there is more than one ocurrence of the same value?
grades = [9, 8 , 10, 10, 7, 9, 2, 2]
#drop the lowest grade
grades.remove(2)
print(grades)

# if you try to remove a value that isn't there
grades.remove(25)

# this is where in becomes useful
if 25 in grades:
    grades.remove(25)
else:
    print("That grade wasn't there")

# the length method - len(list)
len(grades) #tells me how many elements there are in the list

# there will NEVER be a list element whose index is len(list)

grades[len(grades)] # this will NEVER exist; it ALWAYS produces an error
#the last element in any list is ALWAYS
grades[len(grades)-1]