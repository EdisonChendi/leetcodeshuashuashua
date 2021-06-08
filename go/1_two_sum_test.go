package leetcode

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

func twoSum(nums []int, target int) []int {
	remember := make(map[int]int)
	for i, v := range nums {
		if idx, ok := remember[target-v]; ok {
			return []int{idx, i}
		}
		remember[v] = i
	}
	return nil
}

func Test1NormalCase1(t *testing.T) {
	nums := []int{2, 7, 11, 15}
	target := 9
	expected := []int{0, 1}
	res := twoSum(nums, target)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test1NormalCase2(t *testing.T) {
	nums := []int{3, 2, 4}
	target := 6
	expected := []int{1, 2}
	res := twoSum(nums, target)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test1NormalCase3(t *testing.T) {
	nums := []int{3, 3}
	target := 6
	expected := []int{0, 1}
	res := twoSum(nums, target)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
