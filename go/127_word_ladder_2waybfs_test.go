package leetcode

import (
	"testing"
)

func ladderLength(beginWord string, endWord string, wordList []string) int {
	allWords := make(map[string]bool, len(wordList))
	for _, w := range wordList {
		allWords[w] = true
	}
	if _, ok := allWords[endWord]; !ok {
		return 0
	}

	dist := 0
	front := map[string]bool{beginWord: true}
	back := map[string]bool{endWord: true}
	delete(allWords, beginWord)
	delete(allWords, endWord)
	for len(front) > 0 {
		dist += 1
		newFront := make(map[string]bool)
		for word, _ := range front {
			chars := []byte(word)
			for i := 0; i < len(word); i++ {
				temp := chars[i]
				for ch := 'a'; ch <= 'z'; ch++ {
					chars[i] = byte(ch)
					newWord := string(chars)
					if _, ok := back[newWord]; ok {
						return dist + 1
					}
					if _, ok := allWords[newWord]; ok {
						delete(allWords, newWord)
						newFront[newWord] = true
					}
				}
				chars[i] = temp
			}
		}
		front = newFront
		if len(front) < len(back) {
			front, back = back, front
		}
	}
	return 0
}

func Test127NormalCase1(t *testing.T) {
	beginWord := "hit"
	endWord := "cog"
	wordList := []string{"hot", "dot", "dog", "lot", "log", "cog"}
	expected := 5
	res := ladderLength(beginWord, endWord, wordList)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}

func Test127NormalCase2(t *testing.T) {
	beginWord := "hit"
	endWord := "cog"
	wordList := []string{"hot", "dot", "dog", "lot", "log"}
	expected := 0
	res := ladderLength(beginWord, endWord, wordList)
	if res != expected {
		t.Fatalf("expected:%v, but got:%v\n", expected, res)
	}
}
