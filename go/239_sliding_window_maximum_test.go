package leetcode

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

func maxFromSlice(s []int) int {
	// assert len(s) > 0
	m := s[0]
	for _, v := range s {
		if v > m {
			m = v
		}
	}
	return m
}

func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) <= k {
		return []int{maxFromSlice(nums)}
	}
	res := []int{}
	window := []int{}
	for i, n := range nums {
		if len(window) > 0 && window[0] == i-k {
			window = window[1:]
		}
		for len(window) > 0 && nums[window[len(window)-1]] < n {
			window = window[:len(window)-1]
		}
		window = append(window, i)
		if i >= k-1 {
			res = append(res, nums[window[0]])
		}
	}
	return res
}

func Test239NormalCase1(t *testing.T) {
	nums := []int{1, 3, -1, -3, 5, 3, 6, 7}
	k := 3
	result := maxSlidingWindow(nums, k)
	expected := []int{3, 3, 5, 5, 6, 7}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}

func Test239NormalCase2(t *testing.T) {
	nums := []int{1}
	k := 1
	result := maxSlidingWindow(nums, k)
	expected := []int{1}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}

func Test239NormalCase3(t *testing.T) {
	nums := []int{1, -1}
	k := 1
	result := maxSlidingWindow(nums, k)
	expected := []int{1, -1}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}

func Test239NormalCase4(t *testing.T) {
	nums := []int{9, 11}
	k := 2
	result := maxSlidingWindow(nums, k)
	expected := []int{11}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}

func Test239NormalCase5(t *testing.T) {
	nums := []int{4, -2}
	k := 2
	result := maxSlidingWindow(nums, k)
	expected := []int{4}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}

func Test239NormalCase6(t *testing.T) {
	nums := []int{4, -2}
	k := 10
	result := maxSlidingWindow(nums, k)
	expected := []int{4}
	if !cmp.Equal(result, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, result)
	}
}
