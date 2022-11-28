# In-class coding for Monday, November 28

import random
nums = [50000]
length = int(input("how many numbers in the list?"))
for i in range(length):
   nums.append(random.randint(1,1000000))
print(nums)

# is 50000 in the list anywhere?
# linear search
comparisons = 0
i = 0
found = False
while not found and i < len(nums):
   comparisons += 1
   if nums[i] == 50000:
      found = True
      print("it's in location ", i)
   else:
      i += 1
if not found:
   print("it was not there")
print("it took ", comparisons, " comparisons")