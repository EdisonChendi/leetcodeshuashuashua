package leetcode

import (
	"fmt"
	"testing"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prv *ListNode
	nxt := head
	for nxt != nil {
		nxt.Next, prv, nxt = prv, nxt, nxt.Next
	}
	return prv
}

func makeLinkedList(l []int) *ListNode {
	if len(l) == 0 {
		return nil
	}
	sentinel := &ListNode{}
	prv := sentinel
	for _, v := range l {
		node := &ListNode{Val: v}
		prv.Next = node
		prv = node
	}
	return sentinel.Next
}

func printLinkedList(l *ListNode) {
	for l != nil {
		if l.Next != nil {
			fmt.Printf("%v->", l.Val)
		} else {
			fmt.Printf("%v", l.Val)
		}
		l = l.Next
	}
	fmt.Println()
}

func Test206NormalCase1(t *testing.T) {
	ll := makeLinkedList([]int{1, 2, 3, 4, 5})
	printLinkedList(ll)
	res := reverseList(ll)
	printLinkedList(res)
}
