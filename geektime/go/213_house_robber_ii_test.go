package leetcode

import "testing"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	sub_rob := func(start, end, pre, now int) int {
		for i := start; i <= end; i++ {
			pre, now = now, max(now, pre+nums[i])
		}
		return now
	}
	y := sub_rob(1, len(nums)-2, 0, nums[0])
	n := sub_rob(1, len(nums)-1, 0, 0)
	return max(y, n)
}

func Test213NormalCase1(t *testing.T) {
	nums := []int{2, 3, 2}
	expected := 3
	res := rob(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test213NormalCase2(t *testing.T) {
	nums := []int{1, 2, 3, 1}
	expected := 4
	res := rob(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test213EdgeCase1(t *testing.T) {
	nums := []int{0}
	expected := 0
	res := rob(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
