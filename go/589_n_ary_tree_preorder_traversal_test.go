package leetcode

type Node struct {
	Val      int
	Children []*Node
}

func pre(node *Node, accu []int) []int {
	if node == nil {
		return accu
	}
	accu = append(accu, node.Val)
	for _, n := range node.Children {
		accu = pre(n, accu)
	}
	return accu
}

func preorder(root *Node) []int {
	return pre(root, []int{})
}
