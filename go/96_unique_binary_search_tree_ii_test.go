package leetcode

import "testing"

func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 1
	for i := 2; i < n+1; i++ {
		for j := 0; j < i; j++ {
			dp[i] += dp[j] * dp[i-1-j]
		}
	}
	return dp[n]
}

func Test96NormalTest1(t *testing.T) {
	n := 3
	expected := 5
	res := numTrees(n)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test96NormalTest2(t *testing.T) {
	n := 10
	expected := 16796
	res := numTrees(n)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
