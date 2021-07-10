package leetcode

import (
	"math"
	"testing"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxProfit(prices []int) int {
	soFar := 0
	cur := 0
	for i := 1; i < len(prices); i++ {
		cur = max(0, cur+prices[i]-prices[i-1])
		soFar = max(soFar, cur)
	}
	return soFar
}

func maxProfit1(prices []int) int {
	lowest := math.MaxInt64
	profit := 0
	for _, p := range prices {
		if p < lowest {
			lowest = p
		} else {
			if p-lowest > profit {
				profit = p - lowest
			}
		}
	}
	return profit
}

func Test121NormalCase1(t *testing.T) {
	prices := []int{7, 1, 5, 3, 6, 4}
	expected := 5
	res := maxProfit(prices)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test121NormalCase2(t *testing.T) {
	prices := []int{7, 6, 4, 3, 1}
	expected := 0
	res := maxProfit(prices)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test121EdgeCase1(t *testing.T) {
	prices := []int{10}
	expected := 0
	res := maxProfit(prices)
	if expected != res {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
