package leetcode

import "fmt"

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) []int {
	res := []int{}
	if root == nil {
		return res
	}

	q := []*TreeNode{root}
	for len(q) > 0 {
		cur_max := -2147483648
		nxt_q := []*TreeNode{}
		for _, n := range q {
			fmt.Println(n.Val)
			if n.Val > cur_max {
				cur_max = n.Val
			}
			if n.Left != nil {
				nxt_q = append(nxt_q, n.Left)
			}
			if n.Right != nil {
				nxt_q = append(nxt_q, n.Right)
			}
		}
		res = append(res, cur_max)
		q = nxt_q
	}
	return res
}
