# leetcode第15题 https://leetcode-cn.com/problems/3sum/
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    tmp = dict()
    #将列表转换成字典，key为列表值，values为出现次数,并达到去重目的
    for i in range(len(nums)):
        tmp[nums[i]] = tmp.get(nums[i], 0)+1
    left = sorted(filter(lambda x:x<0, tmp))
    right = sorted(filter(lambda x:x>=0, tmp))
    if 0 in tmp and tmp[0]>2:
        res = [[0,0,0]]
    else:
        res = []
    for i in left:
        for j in right:
            mid = -(i+j)
            if mid in tmp:
                #判断是否是i,j本身，如1=-(-2+1)
                if mid in (i, j) and tmp[mid]>1:
                    res.append([i, mid, j])
                elif mid<i or mid>j:
                    res.append([i, mid, j])
    return res

nums = [-2,-1,3]
res = threeSum(nums)
print(res)