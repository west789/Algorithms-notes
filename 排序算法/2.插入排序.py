def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i, 0, -1):
            
            if nums[j]<nums[j-1]:
                nums[j], nums[j-1]=nums[j-1], nums[j]
            else:
                break
    return nums






nums = [5,4,3,2,1,5]
new_nums = insert_sort(nums)
print(new_nums)