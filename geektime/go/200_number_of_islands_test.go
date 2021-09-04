package leetcode

import (
	"testing"
)

func numIslands(grid [][]byte) int {
	m := len(grid)
	n := len(grid[0])

	var dfs func(r, c int) bool
	dfs = func(r, c int) bool {
		if grid[r][c] != '1' {
			return false
		}
		grid[r][c] = '0'
		for _, v := range [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}} {
			ni, nj := r+v[0], c+v[1]
			if ni >= 0 && ni < m && nj >= 0 && nj < n {
				dfs(ni, nj)
			}
		}
		return true
	}

	count := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if dfs(i, j) {
				count++
			}
		}
	}

	return count
}

func Test200NormalCase1(t *testing.T) {
	grid := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	}
	expected := 1
	res := numIslands(grid)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test200NormalCase2(t *testing.T) {
	grid := [][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	}
	expected := 3
	res := numIslands(grid)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
