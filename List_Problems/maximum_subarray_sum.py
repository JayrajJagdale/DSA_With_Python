# nums = [5,4,-1,7,8]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# n = len(nums)
# max_sum = float("-inf")
# for i in range(0,n):
#     total = 0
#     for j in range(i,n):
#         total = total + nums[j]
#         max_sum = max(max_sum,total)
# print(max_sum)

# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5,4,-1,7,8]
n = len(nums)
total = 0
maxi = float("-inf")
for i in range(0,n):
    total += nums[i]
    maxi = max(total,maxi)
    if total < 0:
        total = 0

print(maxi)

