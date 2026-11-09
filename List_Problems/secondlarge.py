## BRUTE FORCE
# nums = [55,32,97,-55,45,88,32,21]
# nums.sort()
# print(nums[-2])

## BETTER SOLUTION
# nums = [55,32,97,-55,45,88,32,21]
# largest = float("-inf")
# second_largest = float("-inf")

# for i in range(len(nums)-1):
#     largest = max(nums[i],largest)
# print(largest) 

# for j in range(len(nums)-1):
#     if nums[j] > second_largest and nums[j] < largest:
#         second_largest = nums[j]
# print(second_largest)

## OPTIMAL SOLUTION
nums = [55,32,97,-55,45,88,32,21,97]
largest = float("-inf")
s_largest = float("-inf")

for i in range(len(nums)-1):
    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]

    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]
print(s_largest)