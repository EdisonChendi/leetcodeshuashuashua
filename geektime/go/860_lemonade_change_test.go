package leetcode

import "testing"

func lemonadeChange(bills []int) bool {
	money := make(map[int]int)
	for _, b := range bills {
		if b == 5 {
			money[5] += 1
		}
		if b == 10 {
			if money[5] == 0 {
				return false
			}
			money[10] += 1
			money[5] -= 1
		}
		if b == 20 {
			if money[10] > 0 && money[5] > 0 {
				money[10] -= 1
				money[5] -= 1
				// money[20] += 1
			} else if money[5] >= 3 {
				money[5] -= 3
				// money[20] += 1
			} else {
				return false
			}
		}
	}
	return true
}

func Test860NormalCase1(t *testing.T) {
	bills := []int{5, 5, 5, 10, 20}
	expected := true
	res := lemonadeChange(bills)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
func Test860NormalCase2(t *testing.T) {
	bills := []int{5, 5, 10}
	expected := true
	res := lemonadeChange(bills)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test860NormalCase3(t *testing.T) {
	bills := []int{10, 10}
	expected := false
	res := lemonadeChange(bills)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test860NormalCase4(t *testing.T) {
	bills := []int{5, 5, 10, 10, 20}
	expected := false
	res := lemonadeChange(bills)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
