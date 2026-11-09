# def rev(arr,left,right):
#     if left >= right:
#         return arr
    
#     arr[left],arr[right] = arr[right],arr[right]
#     left += 1
#     right -= 1
    
#     return rev(arr,left,right)

# print(rev([5,7,3,2,6,1,5,9],2,5))

# Using WHILE loop

arr = [5,7,3,2,6,1,9]
left = 2
right = 5


while(left < right):
    arr[left],arr[right] = arr[right],arr[left]
    left += 1
    right -= 1
print(arr)

    