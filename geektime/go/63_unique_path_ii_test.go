package leetcode

import "testing"

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m, n := len(obstacleGrid), len(obstacleGrid[0])
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 0; i < m; i++ {
		for j := 1; j < n+1; j++ {
			if obstacleGrid[i][j-1] == 1 {
				dp[j] = 0
			} else {
				dp[j] += dp[j-1]
			}
		}
	}
	return dp[n]
}

func Test63NormalCase1(t *testing.T) {
	obstacleGrid := [][]int{
		{0, 0, 0}, {0, 1, 0}, {0, 0, 0},
	}
	expected := 2
	res := uniquePathsWithObstacles(obstacleGrid)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test63NormalCase2(t *testing.T) {
	obstacleGrid := [][]int{
		{0, 1}, {0, 0},
	}
	expected := 1
	res := uniquePathsWithObstacles(obstacleGrid)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test63EdgeCase1(t *testing.T) {
	obstacleGrid := [][]int{
		{0},
	}
	expected := 1
	res := uniquePathsWithObstacles(obstacleGrid)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test63EdgeCase2(t *testing.T) {
	obstacleGrid := [][]int{
		{1},
	}
	expected := 0
	res := uniquePathsWithObstacles(obstacleGrid)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
