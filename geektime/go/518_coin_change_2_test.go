package leetcode

import "testing"

func change(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1

	for _, c := range coins {
		for v := c; v <= amount; v++ {
			dp[v] += dp[v-c]
		}
	}
	return dp[len(dp)-1]
}

func Test518NormalCase1(t *testing.T) {
	amount := 5
	coins := []int{1, 2, 5}
	expected := 4
	res := change(amount, coins)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test518NormalCase2(t *testing.T) {
	amount := 3
	coins := []int{2}
	expected := 0
	res := change(amount, coins)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test518NormalCase3(t *testing.T) {
	amount := 10
	coins := []int{10}
	expected := 1
	res := change(amount, coins)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
