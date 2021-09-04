package leetcode

import "testing"

func majorityElement(nums []int) int {
	var element int
	count := 0
	for _, n := range nums {
		if count == 0 {
			element = n
			count = 1
		} else {
			if n == element {
				count++
			} else {
				count--
			}
		}
	}
	return element
}

func Test169NormalCase1(t *testing.T) {
	nums := []int{3, 2, 3}
	expected := 3
	res := majorityElement(nums)
	if expected != res {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test169NormalCase2(t *testing.T) {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	expected := 2
	res := majorityElement(nums)
	if expected != res {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
