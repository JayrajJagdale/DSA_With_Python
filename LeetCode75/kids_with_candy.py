# candies =[2,3,5,1,3] 
# extraCandies = 3
# candies = [4,2,1,1,2]
# extraCandies = 1
candies = [12,1,12]
extraCandies = 10
n = len(candies)
total = 0
result =[]
maxi = max(candies)
for i in range(0,n):
    total = candies[i] + extraCandies
    if total >= maxi:
        result.append(True)
    else: 
        result.append(False)
print(result)