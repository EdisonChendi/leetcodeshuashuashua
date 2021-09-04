package leetcode

import "testing"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxProfit1(prices []int, fee int) int {
	// dp
	y, n := -prices[0], 0
	for i := 1; i < len(prices); i++ {
		y = max(y, n-prices[i])
		n = max(n, y+prices[i]-fee)
	}
	return n
}
func maxProfit(prices []int, fee int) int {
	// by greedy
	profit := 0
	holding := prices[0] + fee
	for i := 1; i < len(prices); i++ {
		if prices[i]+fee < holding {
			holding = prices[i] + fee
		} else {
			if prices[i] > holding {
				profit += prices[i] - holding
				holding = prices[i]
			}
		}
	}
	return profit
}

func Test714NormalCase1(t *testing.T) {
	prices := []int{1, 3, 2, 8, 4, 9}
	fee := 2
	expected := 8
	res := maxProfit(prices, fee)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test714NormalCase2(t *testing.T) {
	prices := []int{1, 3, 7, 5, 10, 3}
	fee := 3
	expected := 6
	res := maxProfit(prices, fee)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
