package leetcode

import "testing"

func findMin(nums []int) int {
	l, r := 0, len(nums)-1
	var mid int
	for l < r {
		mid = (l + r) >> 1
		if nums[mid] < nums[r] {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return nums[l]
}

func Test153NormalCase1(t *testing.T) {
	nums := []int{3, 4, 5, 1, 2}
	expected := 1
	res := findMin(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test153NormalCase2(t *testing.T) {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	expected := 0
	res := findMin(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test153EdgeCase1(t *testing.T) {
	nums := []int{11, 13, 15, 17}
	expected := 11
	res := findMin(nums)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
