package leetcode

import "testing"

func detectCycle(head *ListNode) *ListNode {
	cache := make(map[*ListNode]bool)
	cur := head
	for cur != nil {
		if _, ok := cache[cur]; ok {
			return cur
		} else {
			cache[cur] = true
			cur = cur.Next
		}
	}
	return nil
}

func Test142NormcalCase1(t *testing.T) {
	n0 := &ListNode{Val: 3}
	n1 := &ListNode{Val: 2}
	n2 := &ListNode{Val: 0}
	n3 := &ListNode{Val: -4}
	n0.Next = n1
	n1.Next = n2
	n2.Next = n3
	n3.Next = n1
	res := detectCycle(n0)
	expected := n1
	if res != n1 {
		t.Fatalf("expect: %v, got: %v\n", expected.Val, res.Val)
	}
}

func Test142NormcalCase2(t *testing.T) {
	n0 := &ListNode{Val: 1}
	n1 := &ListNode{Val: 2}
	n0.Next = n1
	n1.Next = n0
	res := detectCycle(n0)
	expected := n0
	if res != n0 {
		t.Fatalf("expect: %v, got: %v\n", expected.Val, res.Val)
	}
}

func Test142EdgeCase1(t *testing.T) {
	n0 := &ListNode{Val: 1}
	res := detectCycle(n0)
	if res != nil {
		t.Fatalf("expect: %v, got: %v\n", nil, res.Val)
	}
}
