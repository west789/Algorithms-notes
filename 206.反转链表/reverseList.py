class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if head.next == None:
            return head
        l1 = head.next
        l2 = head.next
        l3 = head
        l3.next = None
        while l1.next:
            l1 = l1.next
            l2.next = l3
            l3 = l2
            l2 = l1
        l1.next = l3
        return l1

n1, n2, n3, n4, n5=ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None
# while n1:
#     print(n1.value)
#     n1 = n1.next

res = Solution().reverseList(n1)
while res:
    print(res.value)
    res = res.next