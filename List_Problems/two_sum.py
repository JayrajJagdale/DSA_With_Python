## BRUTE FORCE
# nums = [5,9,1,2,4,15,6,3]
# target = 13
# n = len(nums) 
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if nums[i] + nums[j] == target:
#             print(i,j)

# OPTIMAL APPROACH
nums = [5,9,1,2,4,15,6,3]
target = 13
hash_map = {}
n = len(nums)
for i in range(0,n):
    remaining = target - nums[i]
    if remaining in hash_map:
        print(hash_map[remaining],i)

    hash_map[nums[i]] = i

