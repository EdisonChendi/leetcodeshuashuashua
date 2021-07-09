package leetcode

import (
	"testing"
)

func initDp(n, amount int) []int {
	res := make([]int, n)
	for i := 1; i < n; i++ {
		res[i] = amount
	}
	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func coinChange(coins []int, amount int) int {
	dp := initDp(amount+1, amount+1)
	for i := 1; i < amount+1; i++ {
		for _, c := range coins {
			if i-c >= 0 {
				dp[i] = min(dp[i], 1+dp[i-c])
			}
		}
	}
	if dp[amount] != amount+1 {
		return dp[amount]
	} else {
		return -1
	}
}

func Test322NormalCase1(t *testing.T) {
	coins := []int{1, 2, 5}
	amount := 11
	expected := 3
	res := coinChange(coins, amount)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test322NormalCase2(t *testing.T) {
	coins := []int{2}
	amount := 3
	expected := -1
	res := coinChange(coins, amount)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test322NormalCase3(t *testing.T) {
	coins := []int{1}
	amount := 0
	expected := 0
	res := coinChange(coins, amount)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test322NormalCase4(t *testing.T) {
	coins := []int{1}
	amount := 1
	expected := 1
	res := coinChange(coins, amount)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test322NormalCase5(t *testing.T) {
	coins := []int{1}
	amount := 2
	expected := 2
	res := coinChange(coins, amount)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
