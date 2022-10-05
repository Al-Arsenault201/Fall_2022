# file number 2 from in-class coding Wednesday October 5

def fourth_root(num):
    print(id(num))
    y = num**(1/4)# num**0.25
#    print ("The fourth root of ", num, " is ", y)
    return y

if __name__ == "__main__":
    num = int(input("Enter the number whose fourth root we will calculate"))
    print(id(num))
    y = fourth_root(num)
    print("The fourth root of ", num, " is ", y)