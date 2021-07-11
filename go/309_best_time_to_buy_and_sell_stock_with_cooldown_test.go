package leetcode

import "testing"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxProfit(prices []int) int {
	hold, cool, not_hold := -prices[0], 0, 0
	for i := 1; i < len(prices); i++ {
		hold, cool, not_hold = max(hold, cool-prices[i]), max(cool, not_hold), max(not_hold, hold+prices[i])
	}
	return not_hold
}

func Test309NormalCase1(t *testing.T) {
	prices := []int{1, 2, 3, 0, 2}
	expected := 3
	res := maxProfit(prices)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test309NormalCase2(t *testing.T) {
	prices := []int{1}
	expected := 0
	res := maxProfit(prices)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
