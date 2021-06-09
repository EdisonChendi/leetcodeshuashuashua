package leetcode

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorder(node *TreeNode, accu []int) []int {
	if node == nil {
		return accu
	}
	return inorder(node.Right, append(inorder(node.Left, accu), node.Val))
}

func inorderTraversal(root *TreeNode) []int {
	return inorder(root, []int{})
}

func Test94NormalCase1(t *testing.T) {
	tree := TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 3,
			},
		},
	}
	expected := []int{1, 3, 2}
	res := inorderTraversal(&tree)
	if !cmp.Equal(expected, res) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test94NormalCase2(t *testing.T) {
	tree := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
	}
	expected := []int{2, 1}
	res := inorderTraversal(&tree)
	if !cmp.Equal(expected, res) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test94NormalCase3(t *testing.T) {
	tree := TreeNode{
		Val: 1,
		Right: &TreeNode{
			Val: 2,
		},
	}
	expected := []int{1, 2}
	res := inorderTraversal(&tree)
	if !cmp.Equal(expected, res) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
