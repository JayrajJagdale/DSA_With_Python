def selectSort(num):
    n = len(num)
    for i in range(0,n):
        mini_ind = i
        for j in range(i+1,n):
            if num[j] < num[mini_ind]:
                mini_ind = j
        num[i],num[mini_ind] = num[mini_ind],num[i]
    return num

print(selectSort([1,7,8,4,5,6,9,2]))