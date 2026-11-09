# Brute Force
# n = 7
# nums = []

# for i in range(1,n+1):
#      if n % i == 0:
#         nums.append(i)
# print(nums)

# Better Solution
# n = 10
# result = []
# for i in range(1,(n//2)+1):
#     if n % i == 0:
#         result.append(i)
# result.append(n)
# print(result)

# Optimal Solution
from math import sqrt
results = []
n = 36
num = n
for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        results.append(i)
        if num // i != i:
            results.append(num // i)
print(results)