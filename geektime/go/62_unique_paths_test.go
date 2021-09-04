package leetcode

import "testing"

func makeSlice(v, len int) []int {
	res := make([]int, len)
	for i := 0; i < len; i++ {
		res[i] = v
	}
	return res
}

func uniquePaths(m int, n int) int {
	dp := makeSlice(1, n)
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[j] += dp[j-1]
		}
	}
	return dp[n-1]
}

func Test62NormalCase1(t *testing.T) {
	m := 3
	n := 2
	expected := 3
	res := uniquePaths(m, n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test62NormalCase2(t *testing.T) {
	m := 3
	n := 7
	expected := 28
	res := uniquePaths(m, n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test62NormalCase3(t *testing.T) {
	m := 7
	n := 3
	expected := 28
	res := uniquePaths(m, n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test62NormalCase4(t *testing.T) {
	m := 3
	n := 3
	expected := 6
	res := uniquePaths(m, n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
