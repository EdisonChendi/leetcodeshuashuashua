package leetcode

import (
	"sort"
	"testing"

	"github.com/google/go-cmp/cmp"
)

func threeSum(nums []int) [][]int {
	res := [][]int{}
	if len(nums) < 3 {
		return res
	}
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}
		ni := nums[i]
		j, k := i+1, len(nums)-1
		for j < k {
			nj, nk := nums[j], nums[k]
			if nj+nk == -ni {
				res = append(res, []int{ni, nj, nk})
				j++
				for j < k && nums[j-1] == nums[j] {
					j++
				}
				k--
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else if nj+nk < -ni {
				j++
			} else {
				k--
			}
		}
	}
	return res
}

func Test15NormalCase1(t *testing.T) {
	nums := []int{-1, 0, 1, 2, -1, -4}
	expected := [][]int{
		{-1, -1, 2},
		{-1, 0, 1},
	}
	res := threeSum(nums)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expect: %v, got: %v\n", expected, res)
	}
}

func Test15EdgeCase1(t *testing.T) {
	nums := []int{}
	expected := [][]int{}
	res := threeSum(nums)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expect: %v, got: %v\n", expected, res)
	}
}

func Test15EdgeCase2(t *testing.T) {
	nums := []int{0}
	expected := [][]int{}
	res := threeSum(nums)
	if !cmp.Equal(res, expected) {
		t.Fatalf("expect: %v, got: %v\n", expected, res)
	}
}
