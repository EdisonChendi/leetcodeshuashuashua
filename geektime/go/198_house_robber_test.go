package leetcode

import "testing"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	pre, now := 0, 0
	for i := 0; i < len(nums); i++ {
		pre, now = now, max(now, pre+nums[i])
	}
	return now
}

func Test198NormalCase1(t *testing.T) {
	nums := []int{1, 2, 3, 1}
	expected := 4
	res := rob(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test198NormalCase2(t *testing.T) {
	nums := []int{2, 7, 9, 3, 1}
	expected := 12
	res := rob(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
