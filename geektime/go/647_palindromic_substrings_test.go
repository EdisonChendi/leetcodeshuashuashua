package leetcode

import (
	"testing"
)

func initDp647(n int) [][]bool {
	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
	}
	return dp
}

func countSubstrings(s string) int {
	N := len(s)
	dp := initDp647(N)
	count := 0
	seen := make(map[byte][]int)
	for i := 0; i < N; i++ {
		if ids, ok := seen[s[i]]; ok {
			for _, j := range ids {
				if i-j == 1 || dp[j+1][i-1] {
					dp[j][i] = true
					count += 1
				}
			}
		}
		seen[s[i]] = append(seen[s[i]], i)
		dp[i][i] = true
		count += 1
	}
	return count
}

func Test647NormalCase1(t *testing.T) {
	s := "abc"
	expected := 3
	res := countSubstrings(s)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test647NormalCase2(t *testing.T) {
	s := "aaa"
	expected := 6
	res := countSubstrings(s)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test647NormalCase3(t *testing.T) {
	s := "abccba"
	expected := 9
	res := countSubstrings(s)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
