def lSearch(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = [5,3,9,8,1,6,4,-10,-10]
target = 4
nums1 = [10,20,25,10,10,-3,-5]
target1 = 10
nums2 = [5,3,9,8,1,6,4,-10,-10]
target2 = 100
print(lSearch(nums2,target2))