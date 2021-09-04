package leetcode

import (
	"math"
	"testing"
)

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func helper(node *TreeNode, lower int, upper int) bool {
	return node == nil ||
		node.Val > lower && node.Val < upper &&
			helper(node.Left, lower, node.Val) && helper(node.Right, node.Val, upper)
}

func isValidBST(root *TreeNode) bool {
	return helper(root, math.MinInt64, math.MaxInt64)
}

func Test98NormalCase1(t *testing.T) {
	tree := TreeNode{
		Val:   2,
		Left:  &TreeNode{Val: 1},
		Right: &TreeNode{Val: 3},
	}
	res := isValidBST(&tree)
	expected := true
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test98NormalCase2(t *testing.T) {
	tree := TreeNode{
		Val:  5,
		Left: &TreeNode{Val: 1},
		Right: &TreeNode{
			Val: 4,
			Left: &TreeNode{
				Val: 3,
			},
			Right: &TreeNode{
				Val: 6,
			},
		},
	}
	res := isValidBST(&tree)
	expected := false
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
