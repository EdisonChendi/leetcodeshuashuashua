package leetcode

import "testing"

func max(i, j int) int {
	if i > j {
		return i
	} else {
		return j
	}
}

func min(i, j int) int {
	if i < j {
		return i
	} else {
		return j
	}
}

func maxArea(height []int) int {
	res := 0
	i, j := 0, len(height)-1
	for i < j {
		area := min(height[i], height[j]) * (j - i)
		res = max(res, area)
		if height[i] < height[j] {
			i++
		} else {
			j--
		}
	}
	return res
}

func TestMaxArea1(t *testing.T) {
	height := []int{1, 1}
	expected := 1
	res := maxArea(height)
	if res != expected {
		t.Fatalf("expect: %d, got: %d\n", expected, res)
	}
}

func TestMaxArea2(t *testing.T) {
	height := []int{1, 1}
	expected := 1
	res := maxArea(height)
	if res != expected {
		t.Fatalf("expect: %d, got: %d\n", expected, res)
	}
}

func TestMaxArea3(t *testing.T) {
	height := []int{4, 3, 2, 1, 4}
	expected := 16
	res := maxArea(height)
	if res != expected {
		t.Fatalf("expect: %d, got: %d\n", expected, res)
	}
}

func TestMaxArea4(t *testing.T) {
	height := []int{1, 2, 1}
	expected := 2
	res := maxArea(height)
	if res != expected {
		t.Fatalf("expect: %d, got: %d\n", expected, res)
	}
}
