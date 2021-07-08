package leetcode

import (
	"math"
	"testing"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxProduct(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	m := math.MinInt32
	dp := []int{0, 0}
	for _, n := range nums {
		if n >= 0 {
			dp[0], dp[1] = max(n, n*dp[0]), n*dp[1]
		} else {
			dp[0], dp[1] = n*dp[1], min(n, n*dp[0])
		}
		m = max(m, dp[0])
	}
	return m
}

func Test152NormalCase1(t *testing.T) {
	nums := []int{2, 3, -2, 4}
	expected := 6
	res := maxProduct(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test152NormalCase2(t *testing.T) {
	nums := []int{-2, 0, -1}
	expected := 0
	res := maxProduct(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test152NormalCase3(t *testing.T) {
	nums := []int{2, 3, -2, 4, -2, 0, -1}
	expected := 96
	res := maxProduct(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
