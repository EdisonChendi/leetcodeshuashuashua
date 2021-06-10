package leetcode

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

// Definition for a binary tree node.

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorder(node *TreeNode, accu []int) []int {
	if node == nil {
		return accu
	}
	return preorder(node.Right, preorder(node.Left, append(accu, node.Val)))
}

func preorderTraversal(root *TreeNode) []int {
	return preorder(root, []int{})
}

func Test144NormlCase1(t *testing.T) {
	root := TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
	}
	expected := []int{1, 2, 3}
	res := preorderTraversal(&root)
	if !cmp.Equal(expected, res) {
		t.Fatalf("expect: %v, got: %v\n", expected, res)
	}
}

func Test144NormlCase2(t *testing.T) {
	root := TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
		},
	}
	expected := []int{1, 2}
	res := preorderTraversal(&root)
	if !cmp.Equal(expected, res) {
		t.Fatalf("expect: %v, got: %v\n", expected, res)
	}
}
