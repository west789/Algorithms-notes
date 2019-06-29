def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums)-i):
            if nums[j-1]>nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums


if __name__ == '__main__':
    nums = [5, 1, 9, 56, 99, 33, 1, 6]
    print(nums)
    print(bubble_sort(nums))
