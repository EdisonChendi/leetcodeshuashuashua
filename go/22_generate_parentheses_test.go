package leetcode

import (
	"sort"
	"testing"

	"github.com/google/go-cmp/cmp"
)

func sub(l, r, n int, cur string, res []string) []string {
	if l == n && r == n {
		res = append(res, cur)
		return res
	}
	if l < n {
		res = sub(l+1, r, n, cur+"(", res)
	}
	if l > r {
		res = sub(l, r+1, n, cur+")", res)
	}
	return res
}

func generateParenthesis(n int) []string {
	return sub(0, 0, n, "", []string{})
}

func Test22NormalCase1(t *testing.T) {
	n := 3
	expected := []string{
		"((()))",
		"(()())",
		"(())()",
		"()(())",
		"()()()",
	}
	res := generateParenthesis(n)
	trans := cmp.Transformer("Sort", func(in []string) []string {
		out := append([]string(nil), in...)
		sort.Strings(out)
		return out
	})
	if !cmp.Equal(res, expected, trans) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test22NormalCase2(t *testing.T) {
	n := 1
	expected := []string{
		"()",
	}
	res := generateParenthesis(n)
	trans := cmp.Transformer("Sort", func(in []string) []string {
		out := append([]string(nil), in...)
		sort.Strings(out)
		return out
	})
	if !cmp.Equal(res, expected, trans) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}

func Test22NormalCase3(t *testing.T) {
	n := 2
	expected := []string{
		"()()",
		"(())",
	}
	res := generateParenthesis(n)
	trans := cmp.Transformer("Sort", func(in []string) []string {
		out := append([]string(nil), in...)
		sort.Strings(out)
		return out
	})
	if !cmp.Equal(res, expected, trans) {
		t.Fatalf("expected: %v, but got: %v\n", expected, res)
	}
}
