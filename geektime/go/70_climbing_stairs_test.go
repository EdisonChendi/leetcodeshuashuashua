package leetcode

import "testing"

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	f1, f2 := 1, 2
	for i := 2; i < n; i++ {
		f1, f2 = f2, f1+f2
	}
	return f2
}

func Test70NormalCase1(t *testing.T) {
	n := 2
	expected := 2
	res := climbStairs(n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test70NormalCase2(t *testing.T) {
	n := 3
	expected := 3
	res := climbStairs(n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test70NormalCase3(t *testing.T) {
	n := 4
	expected := 5
	res := climbStairs(n)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
