package main

import "fmt"

// import "fmt"

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head != nil {
		slow := head
		fast := head
		for fast != nil && fast.Next != nil {
			slow = slow.Next
			fast = fast.Next.Next
			if fast == slow {
				return true
			}
		}
	}
	return false
}
func main() {
	var n1 = new(ListNode)
	var n2 = new(ListNode)
	var n3 = new(ListNode)
	var n4 = new(ListNode)
	n1.Val, n1.Next = 3, n2
	n2.Val, n2.Next = 0, n3
	n3.Val, n3.Next = 2, n4
	n4.Val, n4.Next = 4, n2
	res := hasCycle(n1)
	fmt.Println(res)
}
