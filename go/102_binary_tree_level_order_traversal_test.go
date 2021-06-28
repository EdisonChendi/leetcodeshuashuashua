package leetcode

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	res := [][]int{}
	q := []*TreeNode{root}

	for len(q) > 0 {
		nxt_q := make([]*TreeNode, 0)
		cur := []int{}
		for len(q) > 0 {
			n := q[0]
			q = q[1:]
			cur = append(cur, n.Val)
			if n.Left != nil {
				nxt_q = append(nxt_q, n.Left)
			}
			if n.Right != nil {
				nxt_q = append(nxt_q, n.Right)
			}
		}
		res = append(res, cur)
		q = nxt_q
	}
	return res
}
