"""
    1) Reverse singly-linked list
    2) Detect cycle in a list
    3) Merge two sorted lists
    4) Remove nth node from the end
    5) Find middle node
    Author: Wenru
"""
from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


# 1) Reverse singly-linked list
def reverse(head: Node) -> Optional[Node]:
    reverse_head = None
    while head:
        next = head.next
        head.next = reverse_head
        reverse_head = head
        head = next
    return reverse_head


# 2) Detect cycle in a list
def is_detect_cycle(head: Node) -> Optional[Node]:
    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    return has_cycle


# 3) Merge two sorted lists
def merge_two_sort(node_1: Node, node_2: Node):
    if node_1 and node_2:
        left = node_1
        right = node_2
        new_node = Node(666)
        head = new_node
        while left and right:
            if left.data <= right.data:
                new_node.next = left
                left = left.next
            else:
                new_node.next = right
                right = right.next
            new_node = new_node.next
        if left:
            new_node.next = right
        if right:
            new_node.next = right
        return head.next
    return node_1 or node_2


# print the linklist
def print_all(node: Node):
    current = node
    if current:
        print(current.data, end="")
        current = current.next
    while current:
        print(f" -> {current.data}", end="")
        current = current.next
    print("\n", flush=True)


# 4) Remove nth node from the end
def remove_nth_node(head: Node, num: int):
    fast = head
    count = 0
    while fast and count < num:
        fast = fast.next
        count += 1
    if not fast and count < num:
        return head
    if not fast and count == num:
        return head.next
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


# 5) Find middle node
def find_middle_node(head: Node):
    slow = head
    fast = head
    fast = fast.next if fast else None
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


if __name__ == "__main__":
    a = Node(0)
    a1 = a
    for i in range(1, 7):
        a.next = Node(i)
        a = a.next
    print("1) Reverse singly-linked list")
    print("original:", end="")
    print_all(a1)
    a2 = reverse(a1)
    print("reverse:", end="")
    print_all(a2)
    print("2) Detect cycle in a list")
    print("original:", end="")
    print(is_detect_cycle(a2))
    b1, b2, b3, b4, b5 = Node(0), Node(1), Node(2), Node(3), Node(4)
    b1.next, b2.next, b3.next, b4.next, b5.next = b2, b3, b4, b5, b3
    # print_all(b1)
    print(is_detect_cycle(b1))
    print("3) Merge two sorted lists")
    c = Node(0)
    c1 = c
    for i in range(2, 10, 2):
        c.next = Node(i)
        c = c.next
    print("Node1:", end="")
    print_all(c1)
    d = Node(1)
    d1 = d
    for j in range(3, 11, 2):
        d.next = Node(j)
        d = d.next
    print("Node2:", end="")
    print_all(d1)
    new_node = merge_two_sort(c1, d1)
    print("new_node", end="")
    print_all(new_node)
    print("4) Remove nth node from the end")
    print_all(d1)
    e1 = remove_nth_node(d1, 10)
    print("after remove 2:", end="")
    print_all(e1)
    print("# 5) Find middle node")
    print("odd number original:", end="")
    print_all(e1)
    f1 = find_middle_node(e1)
    print("original:", end="")
    f2 = Node(0)
    f2.next = e1
    print_all(f2)
    f3 = find_middle_node(f2)
    print(f3.data)