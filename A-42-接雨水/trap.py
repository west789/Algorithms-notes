def trap(nums):
    movepeak = 0
    triprain = 0
    maxindex = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[maxindex]:
            maxindex = i
    
    for j in range(maxindex):
        if movepeak < nums[j]:
            movepeak = nums[j]
        else:
            triprain += movepeak - nums[j]
    
    movepeak = 0

    for k in range(len(nums)-1, maxindex, -1):
        if movepeak < nums[k]:
            movepeak = nums[k]
        else:
            triprain += movepeak - nums[k]
    
    return triprain

# def trap(listp):
#     """
#     :type height: List[int]
#     :rtype: int
#     """
#     #记录指针移动过程中的高峰
#     movepeak = 0
#     #记录最大面积
#     triprain = 0
#     #记录整体最大木板的index
#     maxindex = 0
#     #先遍历数组找到最大那块板的index
#     for i in range(1, len(listp)):
#         if listp[i] > listp[maxindex]:
#             maxindex = i
#     #再从前往后向maxindex那里遍历
#     #这里不用担心右边的木板最终会比我们的Movepeak小，因为我们有maxindex挡着
#     for i in range(0, maxindex):
        
        
#         if movepeak < listp[i]:
#             #遇到新的高峰，就更新我们的移动最高峰，标志着上一段结束了，接下来应该用新高峰去计算
#             movepeak = listp[i]
#         else:
#             #因为每次前进一步，所以面积的宽度始终为1，也就不用写了
#             triprain += movepeak - listp[i]
#     #重置高峰
#     movepeak = 0
#     #从右向左遍历
#     for j in range(len(listp) - 1, maxindex, -1):
#         #类似的思路
#         #因为有maxindex的存在，使得我们的面积可以不断肆无忌惮的更新
#         if movepeak < listp[j]:
#             movepeak = listp[j]
#         else:
#             triprain += movepeak - listp[j]
#     return triprain

nums =  [0,1,0,2,1,0,1,3,2,1,2,1]
res = trap(nums)
print(res)