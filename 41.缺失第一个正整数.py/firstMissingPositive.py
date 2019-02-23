def firstMissingPositive(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 80+ ms第一种方式
        j = 1
        nums_new = sorted(filter(lambda x:x>0, nums))
        print(nums_new)
        for i in range(len(nums_new)):
            if (i>0 and nums_new[i]==nums_new[i-1]):
                continue
            if nums_new[i] == j:
                j += 1
            else:
                return j
        return j

#44 ms 第二种方式
def firstMissingPositive1(nums):
    n = 1
    while n in nums:
        n += 1
    return n

nums = [1, 2]
print(firstMissingPositive(nums))