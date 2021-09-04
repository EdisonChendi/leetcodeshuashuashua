package leetcode

import (
	"testing"
)

func exclude(nums []int, idx int) []int {
	var res []int
	for i, n := range nums {
		if i != idx {
			res = append(res, n)
		}
	}
	return res
}

func permute(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{{}}
	}
	res := [][]int{}
	for i, n := range nums {
		for _, r := range permute(exclude(nums, i)) {
			res = append(res, append(r, n))
		}
	}
	return res
}

func Test46NormalCase1(t *testing.T) {
	nums := []int{1, 2, 3}
	// expected := [][]int{{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}}
	t.Logf("%v\n", permute(nums))
}

// func Test46NormalCase2(t *testing.T) {
// 	nums := []int{0, 1}
// 	// expected := [][]int{{0, 1}, {1, 0}}
// 	t.Logf("%v\n", permute(nums))
// }

// func Test46NormalCase3(t *testing.T) {
// 	nums := []int{1}
// 	// expected := [][]int{{1}}
// 	t.Logf("%v\n", permute(nums))
// }
