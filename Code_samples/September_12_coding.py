# coding in-class on Monday, September 12

# getting data from a user
# the input statement

#answer = input("whatever we want as a prompt")
#print(answer)

#let's give the user a little help
print("Enter the value asked for; hit 'Enter' when you're done")
new_answer = input("How old is your dog?")
print(new_answer)


#why can't I include everything above in an input statement?
new_answer = input("How old is your dog?", "hit Enter when you're done")
print(new_answer)

#the prompt for an input statement must be a single string
# input can use a string variable as a prompt
name = input("please enter your name")
age = input(name)
print(age)


age = input("What is your dog's age?")
#age is always a string variable - that's how Python works
print(age)

# we can't do subtraction with strings
age = input("What is your dog's age?")
print(age - 2)

# print a literal
print("Hello, world")
print(42)
print(3.14159)
print(True)

#print multiple values
print("Hello, world",42,3.14159,True)
# the comma causes Python to print one blank space then the next value

# print a literal
print("Hello, world", end="first line")
print(42, end="abc")
print(3.14159, end="    ")
print(True, end="123")

print("Hello, world", end="    ")
print(42, end="    ")
print(3.14159, end="    ")
print(True)
print("we're done")

#built-in functions in Python
# int - converts from whatever type to an integer - change "6" to 6
# float - converts from whatever type to a floating point number - change "6"to 6.0
# str - converts from whatever type to a string - change 6.0 to "6.0"

#if we want to input an integer, we read in the string and use int to cast to an integer
age = input("Enter your dog's age")
real_age = int(age)# age is a string; real_age is an integer
print("The dog is", real_age, "years old")


# a simpler way to do this
age = int(input("Enter your dog's age"))
print(age)

# int and float ONLY work if the user input something that can actually be a number


# The ** operator in Python is exponentiation
y = 4**2   # y = 4 to the second power - 4 squared
y = 4**3   # y = 4 cubed - 64
y = 4**(1/2)  # y = 4 to the one-half power, or square root

