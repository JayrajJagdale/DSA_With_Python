# # BRUTE FORCE

nums = [3,9,5,6,7,2]
k = 7   
n = len(nums)
rotations = k % n

for _ in range(0,rotations):
    e = nums.pop()
    nums.insert(0,e)
print(nums)


## BETTER SOLUTION
# nums = [3,9,5,6,7,2,10,9]
# n = len(nums)
# k = 5
# nums[:] = nums[n-k:] + nums[:n-k]

## OR
# nums = [3,9,5,6,7,2,10,9]
# n = len(nums)
# k = 5
# k =  k % n
# print(k)
# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)

## OPTIMAL SOLUTION

# def rotateK(nums,left,right):
#     while left < right:
#         nums[left],nums[right] = nums[right],nums[left]
#         left += 1
#         right -= 1
#     return nums


# nums = [3,9,5,6,7,2,10,9]
# k = 5
# n = len(nums)
# rotateK(nums,n-k,n-1)
# rotateK(nums,0,n-k-1)
# print(rotateK(nums,0,n-1))
