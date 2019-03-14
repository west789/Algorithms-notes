def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if nums[min]>nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums








nums = [5,4,3,2,1,5]
new_nums = select_sort(nums)
print(new_nums)