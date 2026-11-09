## BRUTE FORCE
# nums = [1,1,1,2,3,4,4,7,9,9,9,10]
# n = len(nums)
# freq_map =  {}

# for i in range(0,n):
#     freq_map[nums[i]] = 0

# j = 0
# for k in freq_map:
#     nums[j] = k
#     j += 1

# print(j)

## OPTIMAL Solution
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)
if n == 1:
    print(1)
i = 0
j = i + 1
while(j < n):
    if nums[i] != nums[j]:
        i+=1
        nums[i],nums[j] = nums[j],nums[i]
    j+=1
print(i+1)
print(nums)