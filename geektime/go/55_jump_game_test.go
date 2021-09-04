package leetcode

import "testing"

func canJump_solution2(nums []int) bool {
	target := len(nums) - 1
	for i := target; i >= 0; i-- {
		if i+nums[i] >= target {
			target = i
		}
	}
	return target == 0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func canJump(nums []int) bool {
	reachable := 0
	for i, v := range nums {
		if i > reachable {
			return false
		}
		reachable = max(i+v, reachable)
	}
	return true
}

func Test55NormalCase1(t *testing.T) {
	nums := []int{2, 3, 1, 1, 4}
	expected := true
	res := canJump(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test55NormalCase2(t *testing.T) {
	nums := []int{3, 2, 1, 0, 4}
	expected := false
	res := canJump(nums)
	if res != expected {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
