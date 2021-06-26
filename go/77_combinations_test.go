package leetcode

import (
	"fmt"
	"testing"
)

func combineHelper(n int, start int, left int, cur []int, accu [][]int) [][]int {
	if left == 0 {
		t := make([]int, len(cur))
		copy(t, cur)
		return append(accu, t)
	}
	for i := start; i <= n-left+1; i++ {
		cur = append(cur, i)
		accu = combineHelper(n, i+1, left-1, cur, accu)
		cur = cur[:len(cur)-1]
	}
	return accu
}

func combine(n int, k int) [][]int {
	return combineHelper(n, 1, k, make([]int, 0), make([][]int, 0))
}

func Test77Combine(t *testing.T) {
	n := 5
	k := 4
	fmt.Println(combine(n, k))
}
