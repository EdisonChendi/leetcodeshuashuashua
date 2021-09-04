package leetcode

import "testing"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minimumTotal(triangle [][]int) int {
	for i := len(triangle) - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
		}
	}
	return triangle[0][0]
}

func Test120NormalCase1(t *testing.T) {
	triangle := [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}
	expected := 11
	res := minimumTotal(triangle)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test120NormalCase2(t *testing.T) {
	triangle := [][]int{{-10}}
	expected := -10
	res := minimumTotal(triangle)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
