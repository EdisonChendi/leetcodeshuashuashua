package leetcode

import (
	"testing"
)

func initDp(m, n int) [][]int {
	res := make([][]int, m)
	for i := 0; i < m; i++ {
		res[i] = make([]int, n)
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)
	dp := initDp(m+1, n+1)
	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = 1 + dp[i-1][j-1]
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[m][n]
}

func Test1143NormalCase1(t *testing.T) {
	text1 := "abcde"
	text2 := "ace"
	expected := 3
	res := longestCommonSubsequence(text1, text2)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test1143NormalCase2(t *testing.T) {
	text1 := "abc"
	text2 := "abc"
	expected := 3
	res := longestCommonSubsequence(text1, text2)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test1143NormalCase3(t *testing.T) {
	text1 := "abc"
	text2 := "def"
	expected := 0
	res := longestCommonSubsequence(text1, text2)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
