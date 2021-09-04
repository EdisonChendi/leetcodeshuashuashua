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

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func helper(node *TreeNode) (bool, int, int) {
	if node == nil {
		return true, math.MaxInt64, -math.MaxInt64
	}
	lvalid, lmin, lmax := helper(node.Left)
	if !lvalid || node.Val <= lmax {
		return false, 0, 0
	}

	rvalid, rmin, rmax := helper(node.Right)
	if !rvalid || node.Val >= rmin {
		return false, 0, 0
	}
	return true, min(lmin, node.Val), max(rmax, node.Val)
}

func isValidBST(root *TreeNode) bool {
	res, _, _ := helper(root)
	return res
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
