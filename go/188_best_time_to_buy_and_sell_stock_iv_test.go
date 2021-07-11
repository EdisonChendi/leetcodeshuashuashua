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

func initDp(k int) [][2]int {
	dp := make([][2]int, k)
	for i := 0; i < k; i++ {
		dp[i][0] = math.MinInt64
		dp[i][1] = math.MinInt64
	}
	dp[0][0] = 0
	return dp
}

func maxProfit(k int, prices []int) int {
	if k == 0 || len(prices) <= 1 {
		return 0
	}
	dp := initDp(k)
	profit := 0
	for _, p := range prices {
		for i := 0; i < k; i++ {
			if i > 0 {
				dp[i][0] = max(dp[i][0], dp[i-1][1]+p)
			}
			dp[i][1] = max(dp[i][1], dp[i][0]-p)
		}
		profit = max(profit, dp[k-1][1]+p)
	}
	return profit
}

func Test188NormalCase1(t *testing.T) {
	k := 2
	prices := []int{2, 4, 1}
	expected := 2
	res := maxProfit(k, prices)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test188NormalCase2(t *testing.T) {
	k := 2
	prices := []int{3, 2, 6, 5, 0, 3}
	expected := 7
	res := maxProfit(k, prices)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
