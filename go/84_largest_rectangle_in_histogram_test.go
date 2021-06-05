package leetcode

import (
	"testing"
)

func largestRectangleArea(heights []int) int {
	stack := []int{-1}
	N := len(heights)
	res := 0
	for i, h := range heights {
		for len(stack) > 1 && h < heights[stack[len(stack)-1]] {
			topIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			width := i - stack[len(stack)-1] - 1
			area := heights[topIdx] * width
			if area > res {
				res = area
			}
		}
		stack = append(stack, i)
	}
	for len(stack) > 1 {
		topIdx := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		width := N - stack[len(stack)-1] - 1
		area := heights[topIdx] * width
		if area > res {
			res = area
		}
	}
	return res
}

func Test84NormalCase1(t *testing.T) {
	heights := []int{2, 1, 5, 6, 2, 3}
	expected := 10
	res := largestRectangleArea(heights)
	if expected != res {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test84NormalCase2(t *testing.T) {
	heights := []int{2, 4}
	expected := 4
	res := largestRectangleArea(heights)
	if expected != res {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
