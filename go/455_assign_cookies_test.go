package leetcode

import (
	"sort"
	"testing"
)

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)
	res := 0
	for gi, si := 0, 0; gi < len(g) && si < len(s); si++ {
		if s[si] >= g[gi] {
			res += 1
			gi += 1
		}
	}
	return res
}

func Test455NormalCase1(t *testing.T) {
	g := []int{1, 2, 3}
	s := []int{1, 1}
	expected := 1
	res := findContentChildren(g, s)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test455NormalCase2(t *testing.T) {
	g := []int{1, 2}
	s := []int{1, 2, 3}
	expected := 2
	res := findContentChildren(g, s)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
