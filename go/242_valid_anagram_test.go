package leetcode

import "testing"

func isAnagram2(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counter := make(map[rune]int)
	for _, ch := range s {
		counter[ch] += 1
	}
	for _, ch := range t {
		if _, ok := counter[ch]; !ok {
			return false
		}
		counter[ch] -= 1
		if counter[ch] < 0 {
			return false
		}
	}
	for _, v := range counter {
		if v != 0 {
			return false
		}
	}
	return true
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	table := make([]int, 26)
	for i := 0; i < len(s); i++ {
		table[s[i]-'a']++
		table[t[i]-'a']--
	}
	for i := 0; i < 26; i++ {
		if table[i] != 0 {
			return false
		}
	}
	return true
}

func Test242NormalCase1(t *testing.T) {
	s1 := "anagram"
	s2 := "nagaram"
	expected := true
	res := isAnagram(s1, s2)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}

func Test242NormalCase2(t *testing.T) {
	s1 := "rat"
	s2 := "car"
	expected := false
	res := isAnagram(s1, s2)
	if res != expected {
		t.Fatalf("expected: %v, got: %v\n", expected, res)
	}
}
