package leetcode

import "testing"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	m, pre := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		pre = max(nums[i], pre+nums[i])
		m = max(pre, m)
	}
	return m
}

func Test53NormalCase1(t *testing.T) {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	expected := 6
	res := maxSubArray(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test53NormalCase2(t *testing.T) {
	nums := []int{5, 4, -1, 7, 8}
	expected := 23
	res := maxSubArray(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test53EdgeCase1(t *testing.T) {
	nums := []int{1}
	expected := 1
	res := maxSubArray(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
