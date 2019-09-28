def merge_sort(nums):
    n = len(nums)
    if n<=1:
        return nums
    mid = n//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    new_nums = []
    i, j =0, 0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            new_nums.append(left[i])
            i += 1
        else:
            new_nums.append(right[j])
            j += 1
    new_nums.extend(left[i:])
    new_nums.extend(right[j:])
    return new_nums



nums = [5,4,3,2,1,5,9,6,5,3,566,22,63,3]
new_nums = merge_sort(nums)
print(new_nums)