package leetcode

import (
	"sort"
	"strings"
	"testing"
)

func sortedString(s string) string {
	ss := strings.Split(s, "")
	sort.Strings(ss)
	return strings.Join(ss, "")
}

func sortedString2(s string) string {
	ss := []byte(s)
	sort.Slice(ss, func(i, j int) bool { return ss[i] < ss[j] })
	return string(ss)
}

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, s := range strs {
		ss := sortedString2(s)
		m[ss] = append(m[ss], s)
	}
	var res [][]string
	for _, v := range m {
		res = append(res, v)
	}
	return res
}

func Test49NormalCase1(t *testing.T) {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	t.Log(groupAnagrams(strs))
}
