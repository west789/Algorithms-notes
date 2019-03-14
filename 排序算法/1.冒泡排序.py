def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,4,3,2,1,5]
new_nums = bubble_sort(nums)
print(new_nums)
#时间复杂度O(n^2) 原地排序算法，稳定的排序算法