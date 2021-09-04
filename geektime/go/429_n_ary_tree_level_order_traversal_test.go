package leetcode

type Node struct {
	Val      int
	Children []*Node
}

func level(trees []*Node, accu [][]int) [][]int {
	if len(trees) == 0 {
		return accu
	}
	cur := []int{}
	nxt := []*Node{}
	for _, root := range trees {
		cur = append(cur, root.Val)
		nxt = append(nxt, root.Children...)
	}
	return level(nxt, append(accu, cur))
}

func levelOrder(root *Node) [][]int {
	if root == nil {
		return [][]int{}
	}
	return level([]*Node{root}, [][]int{})
}

func levelOrder2(root *Node) [][]int {
	if root == nil {
		return nil
	}
	var res [][]int
	q := []*Node{root}
	for len(q) > 0 {
		nxt_q := []*Node{}
		cur := make([]int, len(nxt_q))
		for _, n := range q {
			cur = append(cur, n.Val)
			nxt_q = append(nxt_q, n.Children...)
		}
		res = append(res, cur)
		q = nxt_q
	}
	return res
}
