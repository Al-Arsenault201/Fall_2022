
def sum_a_list(nums):
    if len(nums) == 1:
        return(nums[0])
    else:
        n = nums.pop(0)
        return n + sum_a_list(nums)

def recursive_power(num, exponent):
    # base case
    if exponent == 1:
        return num
    else:
        return num * recursive_power(num, exponent-1)

if __name__ == "__main__":
    mynums = [23,38,40, 74]
#    answer = sum_a_list(mynums)
    answer = recursive_power(4,5)
    print(answer)