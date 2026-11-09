## BRUTE FORCE
# def missingNum(nums):
#     n = len(nums)
#     for i in range(0,n+1):
#         if i not in nums:
#             return i
# nums = [3,0,1]
# nums = [9,6,4,2,3,5,7,0,1]
# nums = [1,0,3,4]
# print(missingNum(nums))

## BETTER APPROACH
# nums = [9,6,4,2,3,5,7,0,1]
# freq = {}
# n = len(nums)

# for i in range(0,n+1):
#     freq[i] = 0
# print(freq)

# for num in nums:
#     freq[num] = 1
# print(freq)

# for k,v in freq.items():
#     if v == 0:
#         print(k)

# nums = [9,6,4,2,3,5,7,0,1]
nums = [3,0,1]
n = len(nums)
# sum1 = 0
# sum2 = 0
# for i in range(0,n+1):
#     sum1 += i
# print(sum1)

# for num in nums:
#     sum2 += num
# print(sum2)

# print(sum1-sum2)

print((n * (n+1)//2) - sum(nums))