# in-class coding for Monday, November 7 2022
def recursive_factorial(num):

    # base case
    if num <= 1:
        return 1
    else:

    # recursive case
        intermediate_result = num * recursive_factorial(num-1)
        print("num = ", num, "intermediate result = ", intermediate_result)
        return intermediate_result


if __name__ == "__main__":
    n = 5
    print(recursive_factorial(n))
