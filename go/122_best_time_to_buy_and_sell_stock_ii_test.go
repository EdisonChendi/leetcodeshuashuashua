package leetcode

import "testing"

func maxProfit(prices []int) int {
	res := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i+1] > prices[i] {
			res += prices[i+1] - prices[i]
		}
	}
	return res
}

func Test122NormaCase1(t *testing.T) {
	prices := []int{7, 1, 5, 3, 6, 4}
	expected := 7
	res := maxProfit(prices)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test122NormaCase2(t *testing.T) {
	prices := []int{1, 2, 3, 4, 5}
	expected := 4
	res := maxProfit(prices)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test122NormaCase3(t *testing.T) {
	prices := []int{7, 6, 4, 3, 1}
	expected := 0
	res := maxProfit(prices)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
