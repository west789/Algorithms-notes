#leetcode第169题 https://leetcode-cn.com/problems/majority-element/
def majorityElement(nums):
        itemDict = {}
        for i in range(len(nums)):
            itemDict[nums[i]] = itemDict.get(nums[i], 0)+1
        for i in range(len(nums)):
            if itemDict[nums[i]]>len(nums)//2:
                return nums[i]
            if nums[i+1]==nums[i]:
                continue
# 另一种方式
# def majorityElement(nums):
#         itemDict = {}
#         for i in range(len(nums)):
#             itemDict[nums[i]] = itemDict.get(nums[i], 0)+1
#         return max(itemDict, itemDict.get)

#第三种方式
# def majorityElement(nums):
#     nums=sorted(nums)
#     return nums[int(len(nums)/2)]



nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
