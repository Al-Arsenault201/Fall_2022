"""
First we're just going to print a literal
Literal means "exactly this."
"""
#print("Hello, world")

"""
Now we'll write the program with a variable so it can change
"""
var = "Hello there, world"
print(var)
#print(id(var))
var = "A second value"
print(var)

"""
types: string - 0 or more characters taken together as one variable
int  (integer) - a whole number - positive or negative; no decimal point
float - a real number - positive or negative; decimal point included
boolean - True or False
"""

x = 42
print(x)
# you do not have to declare a variable before using it
# in other languages:  int x

y = 4.9
print(y)

answer = True
print(answer)

#now an error
answer = true
print(answer)

#an uninitialized variable
print(z)

#variable names
joe = 55
j0e = 56
j0_e = 57
1je = 93
_j0e = 85

#you can use underscores, not hyphens
long_variable_name = 5
long-variable-name = 5

#those are Python rules
# a CMSC 201 rule: use snake_case not camelCase
# for long variable names

#camelCase
longVariableName = 1
#snake_case
long_variable_name = 1

