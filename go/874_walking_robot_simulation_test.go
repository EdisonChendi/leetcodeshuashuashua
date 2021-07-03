package leetcode

import (
	"testing"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func trans(obstacles [][]int) map[[2]int]bool {
	res := make(map[[2]int]bool, len(obstacles))
	for _, o := range obstacles {
		res[[2]int{o[0], o[1]}] = true
	}
	return res
}

func walk(px, py, c, x, y int, obstacles map[[2]int]bool) (int, int) {
	var npx, npy int
	for i := 0; i < c; i++ {
		npx, npy = px+x, py+y
		if _, ok := obstacles[[2]int{npx, npy}]; ok {
			break
		}
		px, py = npx, npy
	}
	return px, py
}

func dis(x, y int) int {
	return x*x + y*y
}

func robotSim(commands []int, obstacles [][]int) int {
	res := -1
	x, y := 0, 1
	px, py := 0, 0
	obs := trans(obstacles)
	for _, c := range commands {
		if c == -1 {
			x, y = y, -x
		} else if c == -2 {
			x, y = -y, x
		} else {
			px, py = walk(px, py, c, x, y, obs)
			res = max(res, dis(px, py))
		}
	}
	return res
}

func Test874NormcalCase1(t *testing.T) {
	commands := []int{4, -1, 3}
	obstacles := [][]int{}
	expected := 25
	res := robotSim(commands, obstacles)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test874NormcalCase2(t *testing.T) {
	commands := []int{4, -1, 4, -2, 4}
	obstacles := [][]int{{2, 4}}
	expected := 65
	res := robotSim(commands, obstacles)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
