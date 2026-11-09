## METHOD 1

# nums = [55,32,-97,99,3,6]
# largest = nums[0]
# for i in range(len(nums)-1):
#     # if nums[i] > largest:
#     #     largest = nums[i]
#     largest = max(largest,nums[i])
# print(largest)

## METHOD 2

nums = [55,32,-97,99,3,6]
largest = float("-inf")
for i in range(len(nums)-1):
    # if nums[i] > largest:
    #     largest = nums[i]
    largest = max(largest,nums[i])
print(largest)