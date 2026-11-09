## METHOD 1
# nums = [5,-2,3,9,0,6,10,7]
# n  = len(nums)
# nums[:] = [nums[-1]] + nums[0:n]
# print(nums)

## METHOD 2

nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
    print(nums)

nums[0] = temp
print(nums)