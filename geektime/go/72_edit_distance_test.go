package leetcode

import "testing"

func min72(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func min72_3(a, b, c int) int {
	return min72(min72(a, b), c)
}

func minDistance(word1 string, word2 string) int {
	dp := make([]int, len(word2)+1)
	for i := 0; i < len(word2)+1; i++ {
		dp[i] = i
	}
	for i := 1; i < len(word1)+1; i++ {
		newDp := make([]int, len(word2)+1)
		newDp[0] = i
		for j := 1; j < len(word2)+1; j++ {
			if word1[i-1] == word2[j-1] {
				newDp[j] = dp[j-1]
			} else {
				newDp[j] = 1 + min72_3(newDp[j-1], dp[j], dp[j-1])
			}
		}
		dp = newDp
	}
	return dp[len(dp)-1]
}

func Test72NormalCase1(t *testing.T) {
	word1 := "horse"
	word2 := "ros"
	expected := 3
	res := minDistance(word1, word2)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test72NormalCase2(t *testing.T) {
	word1 := "intention"
	word2 := "execution"
	expected := 5
	res := minDistance(word1, word2)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
