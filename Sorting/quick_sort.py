def partation(nums,low,high):
    pivot = nums[low]
    i = low
    j = high

    while i <  j:
        while nums[i] <= pivot and i <= high-1:
            i += 1
        while nums[j] > pivot and j >= low+1:
            j -= 1

        if i < j:
            nums[i],nums[j] = nums[j],nums[i]

    nums[j],nums[low] = nums[low],nums[j]

    return j

def quick_sort(nums,low,high):
    if low < high:
        partation_index = partation(nums,low,high)
        quick_sort(nums,low,partation_index - 1)
        quick_sort(nums,partation_index+1,high)

    return nums



nums = [4,1,7,6,3,2,8]
print(quick_sort(nums,0,len(nums)-1))