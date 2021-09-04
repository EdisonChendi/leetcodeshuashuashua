package leetcode

import "testing"

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	fast, slow := head.Next, head
	for fast != nil && fast.Next != nil {
		if fast == slow {
			return true
		}
		slow, fast = slow.Next, fast.Next.Next
	}
	return false
}

func Test141NormalCase1(t *testing.T) {
	n0 := &ListNode{Val: 3}
	n1 := &ListNode{Val: 2}
	n2 := &ListNode{Val: 0}
	n3 := &ListNode{Val: -4}
	n0.Next = n1
	n1.Next = n2
	n2.Next = n3
	n3.Next = n1
	if !hasCycle(n0) {
		t.Fatalf("expected: %v, got: %v\n", true, false)
	}
}

func Test141NormalCase2(t *testing.T) {
	n0 := &ListNode{Val: 3}
	n1 := &ListNode{Val: 2}
	n2 := &ListNode{Val: 0}
	n3 := &ListNode{Val: -4}
	n0.Next = n1
	n1.Next = n2
	n2.Next = n3
	if hasCycle(n0) {
		t.Fatalf("expected: %v, got: %v\n", false, true)
	}
}
