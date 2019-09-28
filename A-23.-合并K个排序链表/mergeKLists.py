class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        res_list = list()
        for i in lists:
            while i:
                res_list.append(i.value)
                i = i.next
        res_list.sort()
        print(res_list)
        l = ListNode(0)
        first = l
        while res_list:
            l.next = ListNode(res_list.pop(0))
            l = l.next
        return first.next



n1, n2, n3, n4, n5, n6, n7, n8 = ListNode(1), ListNode(4), ListNode(5),\
ListNode(1), ListNode(3), ListNode(4), ListNode(2), ListNode(6)
n1.next = n2
n2.next = n3
n4.next = n5
n5.next = n6
n7.next = n8
lists = [n1, n4, n7]
res = Solution().mergeKLists(lists)
while res:
    print(res.value)
    res = res.next