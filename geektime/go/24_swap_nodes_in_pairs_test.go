package leetcode

import "testing"

func swapPairs1(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	sentinel := &ListNode{Next: head}
	prv, cur := sentinel, head
	var nxt *ListNode
	for cur != nil && cur.Next != nil {
		nxt = cur.Next
		prv.Next, cur.Next, nxt.Next = cur.Next, nxt.Next, cur
		prv, cur = cur, cur.Next
	}
	return sentinel.Next
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newHead := head.Next
	head.Next, newHead.Next = swapPairs(newHead.Next), head
	return newHead
}

func Test24NormalCase1(t *testing.T) {
	ll := MakeLinkedList([]int{1, 2, 3, 4})
	PrintLinkedList(ll)
	res := swapPairs(ll)
	PrintLinkedList(res)
}

func Test24NormalCase2(t *testing.T) {
	ll := MakeLinkedList([]int{1, 2})
	PrintLinkedList(ll)
	res := swapPairs(ll)
	PrintLinkedList(res)
}
