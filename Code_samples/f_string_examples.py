age = 35
height = 182.5
weight = 82.2
name = "Bentley"
print(f'{name:3} is {age:5} years old and weighs {weight:.2f} kilograms')
print(f'{name:3} is {age:5} years old and weighs {weight:10.5f} kilograms')
# in a print:
# have f or F
# then a single quote  and at the end another
# literals are printed exactly as you type them

#an example for HW2
salary = 105.9264 #in HW2 you calculate this
print(f'Your paycheck for the week will be ${salary:12.2f}')

current_month = int(input("what month is it now"))
time_ahead = int(input('how many months ahead'))
month_number = (current_month + time_ahead)%12
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
    # you gotta

current_month = int(input("current month"))
if current_month < 1 or current_month > 12:
    print("That is not a valid month")
else:
    #all the rest of your code goes here