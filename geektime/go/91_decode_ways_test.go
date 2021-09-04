package leetcode

import (
	"strconv"
	"testing"
)

func valid(s string) int {
	if s[0] == '0' {
		return 0
	}
	if toInt, _ := strconv.ParseInt(s, 10, 32); toInt < 27 {
		return 1
	} else {
		return 0
	}
}

func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}
	dp1, dp2 := 1, 1
	s = "0" + s
	for i := 2; i < len(s); i++ {
		dp1, dp2 = dp2, dp1*valid(s[i-1:i+1])+dp2*valid(string(s[i]))
	}
	return dp2
}

func Test91NormalCase1(t *testing.T) {
	s := "12"
	expected := 2
	res := numDecodings(s)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test91NormalCase2(t *testing.T) {
	s := "226"
	expected := 3
	res := numDecodings(s)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test91NormalCase3(t *testing.T) {
	s := "0"
	expected := 0
	res := numDecodings(s)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test91NormalCase4(t *testing.T) {
	s := "06"
	expected := 0
	res := numDecodings(s)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
