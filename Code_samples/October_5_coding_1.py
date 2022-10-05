# first in-class coding file from Wednesday, October 5

def factorial(num):
    """
    This is a function that returns the factorial of any integer
    We presume 'num' is an integer - positive, negative, or 0
    this function fails if you pass a string or float
    :param num: The integer we're calculating the factorial
    :return: num!
    """

    product = 1
    if num > 0:
        for i in range(1,num+1):
            product *= i
        return product
    elif num == 0:
        return 1
    else: # num is a negative number
        return #1

if __name__ == "__main__":
    factor = int(input("enter the number; we'll calculate the factorial of it"))
    fact = factorial(factor)
    if fact == None:
        print("That factorial is undefined")
    else:
        print (factor, " factorial is ", fact)