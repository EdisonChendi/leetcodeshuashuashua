package leetcode

import (
	"testing"
)

func max32(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func longestValidParentheses(s string) int {
	res := 0
	stack := []int{-1}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				res = max32(res, i-stack[len(stack)-1])
			} else {
				stack = append(stack, i)
			}
		}
	}
	return res
}

func Test32NormcalCase1(t *testing.T) {
	s := "(()"
	expected := 2
	res := longestValidParentheses(s)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
