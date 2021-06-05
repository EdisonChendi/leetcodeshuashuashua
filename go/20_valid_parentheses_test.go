package leetcode

import (
	"testing"
)

func isValid(s string) bool {
	m := map[byte]byte{
		')': '(',
		'}': '{',
		']': '[',
	}
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if _, ok := m[ch]; !ok {
			stack = append(stack, ch)
		} else {
			if len(stack) == 0 || stack[len(stack)-1] != m[ch] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func Test20NormalCase1(t *testing.T) {
	s := "()"
	expected := true
	res := isValid(s)
	if isValid(s) != expected {
		t.Fatalf("got: %v, expected: %v\n", res, expected)
	}
}

func Test20NormalCase2(t *testing.T) {
	s := "()[]{}"
	expected := true
	res := isValid(s)
	if isValid(s) != expected {
		t.Fatalf("got: %v, expected: %v\n", res, expected)
	}

}
func Test20NormalCase3(t *testing.T) {
	s := "(]"
	expected := false
	res := isValid(s)
	if isValid(s) != expected {
		t.Fatalf("got: %v, expected: %v\n", res, expected)
	}
}

func Test20NormalCase4(t *testing.T) {
	s := "([)]"
	expected := false
	res := isValid(s)
	if isValid(s) != expected {
		t.Fatalf("got: %v, expected: %v\n", res, expected)
	}
}

func Test20NormalCase5(t *testing.T) {
	s := "{[]}"
	expected := true
	res := isValid(s)
	if isValid(s) != expected {
		t.Fatalf("got: %v, expected: %v\n", res, expected)
	}
}
