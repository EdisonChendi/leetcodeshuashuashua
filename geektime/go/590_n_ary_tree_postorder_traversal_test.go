package leetcode

type Node struct {
	Val      int
	Children []*Node
}

func post(node *Node, accu []int) []int {
	if node == nil {
		return accu
	}
	for _, n := range node.Children {
		accu = post(n, accu)
	}
	accu = append(accu, node.Val)
	return accu
}

func postorder(root *Node) []int {
	return post(root, []int{})
}
