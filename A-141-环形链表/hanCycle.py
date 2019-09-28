class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

n1, n2, n3, n4=ListNode(3), ListNode(0), ListNode(2), ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n2
res = Solution().hasCycle(n1)
print (res)
