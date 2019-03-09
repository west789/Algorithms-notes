#查找第一等于给定值的元素
def bserarch(nums, value):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = low+((high-low)>>1)
        if nums[mid]>value:
            high = mid-1
        elif nums[mid]<value:
            low = mid+1
        else:
            if mid==0 or nums[mid-1] != value:
                return mid
            else:
                high = mid-1
    return -1
nums = [1,2,5,5,5,5,5,9,11]
res = bserarch(nums, 5)
print(res)