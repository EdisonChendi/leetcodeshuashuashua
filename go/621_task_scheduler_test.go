package leetcode

import (
	"sort"
	"testing"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func leastInterval(tasks []byte, n int) int {
	t := make([]int, 26)
	for _, task := range tasks {
		t[task-'A'] += 1
	}
	sort.Ints(t)
	fMax := t[25]
	idleTime := (fMax - 1) * n
	for i := 24; i >= 0 && t[i] > 0 && idleTime > 0; i-- {
		if t[i] == fMax {
			idleTime -= fMax - 1
		} else {
			idleTime -= t[i]
		}
	}
	if idleTime < 0 {
		idleTime = 0
	}
	return idleTime + len(tasks)
}

func Test621NormalCase1(t *testing.T) {
	tasks := []byte{'A', 'A', 'A', 'B', 'B', 'B'}
	n := 2
	expected := 8
	res := leastInterval(tasks, n)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test621NormalCase2(t *testing.T) {
	tasks := []byte{'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}
	n := 2
	expected := 16
	res := leastInterval(tasks, n)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
