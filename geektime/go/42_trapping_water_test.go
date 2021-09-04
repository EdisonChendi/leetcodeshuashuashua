package leetcode

import "testing"

func trap(height []int) int {
	if len(height) < 3 {
		return 0
	}
	leftMax, rightMax := -1, -1
	l, r := 0, len(height)-1
	res := 0
	var lh, rh int
	for l < r {
		lh, rh = height[l], height[r]
		if lh < rh {
			if lh < leftMax {
				res += leftMax - lh
			} else {
				leftMax = lh
			}
			l++
		} else {
			if rh < rightMax {
				res += rightMax - rh
			} else {
				rightMax = rh
			}
			r--
		}
	}
	return res
}

func Test42NormalCase1(t *testing.T) {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	expected := 6
	res := trap(height)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test42NormalCase2(t *testing.T) {
	height := []int{4, 2, 0, 3, 2, 5}
	expected := 9
	res := trap(height)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
