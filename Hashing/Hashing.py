## Brute Force
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]

# for i in m:
#     count = 0
#     for j in n:
#         if i == j:
#             count += 1
#     print(count)

## Optimal 
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11

for i in n:
    hash_list[i] += 1
for j in m:
        if j < 1 or j > 10:
            print(0)
        else:
            print(hash_list[j])


## Using Dictionary
# n = [5,3,2,2,1,5,5,7,5,10]
# m = [10,111,1,9,5,67,2]
# freq_map = {}

# for i in n:
#     freq_map[i] = freq_map.get(i,0)+1
# print(freq_map)
# for j in m:
#     if j in freq_map:
#         print(freq_map[j])
#     else:
#         print(0)

## Character Hashing
# S = "azyxyyzaaaa"
# q = ["d","a","y","x"]
# hash_list = [0] * 26 

# for ch in S:
#     ascii_val = ord(ch)
#     index = ascii_val - 97
#     hash_list[index] += 1

# for char in q:
#     ascii_val = ord(char)
#     index = ascii_val - 97
#     print(hash_list[index])
    



   