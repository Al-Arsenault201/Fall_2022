# In-class coding from Monday, October 3

def cube(num):  # function definition
    """
    This function calculates the cube of an integer
    :param num:
    :return: the cube of num
    """
    answer = num * num * num  # or num**3 or...
    return answer # this value is (sort of) the only thing passed back to the main program
                    #return means end the function & pass some value or None back to the main program

# now define the main program
if __name__ == "__main__":  # this tells Python that what follows is the main program
    x = int(input("Enter a number; I'll find the cube and print it"))
    y = cube(x)      #this is the function call
    print ("The cube of ", x, " is ", y)


