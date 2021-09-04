package leetcode

import (
	"sort"
	"testing"
)

func searchMatrix2(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	l, r := 0, m*n-1
	for l <= r {
		mid := (l + r) >> 1
		v := matrix[mid/n][mid%n]
		if v == target {
			return true
		}
		if target > v {
			l, r = mid+1, r
		} else {
			l, r = l, mid-1
		}
	}
	return false
}

func searchMatrix(matrix [][]int, target int) bool {
	m, n := len(matrix), len(matrix[0])
	i := sort.Search(m*n, func(i int) bool {
		return matrix[i/n][i%n] >= target
	})
	return i < m*n && matrix[i/n][i%n] == target
}

func Test74NormalCase1(t *testing.T) {
	matrix := [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}
	target := 3
	expected := true
	res := searchMatrix(matrix, target)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test74NormalCase2(t *testing.T) {
	matrix := [][]int{{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}}
	target := 13
	expected := false
	res := searchMatrix(matrix, target)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
