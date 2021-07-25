package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type TrieNode struct {
	children  map[rune]*TrieNode
	endOfWord bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{
		children:  make(map[rune]*TrieNode),
		endOfWord: false,
	}
}

type Trie struct {
	root *TrieNode
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{
		root: NewTrieNode(),
	}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	node := this.root
	for _, ch := range word {
		if _, ok := node.children[ch]; ok {
			node = node.children[ch]
		} else {
			node.children[ch] = NewTrieNode()
			node = node.children[ch]
		}
	}
	node.endOfWord = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	node := this.startsWith(word)
	return node != nil && node.endOfWord
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	return this.startsWith(prefix) != nil
}

func (this *Trie) startsWith(s string) *TrieNode {
	node := this.root
	for _, ch := range s {
		if _, ok := node.children[ch]; !ok {
			return nil
		}
		node = node.children[ch]
	}
	return node
}

func Test208NormcalCase1(t *testing.T) {
	trie := Constructor()
	trie.Insert("apple")
	assert.True(t, trie.Search("apple"))
	assert.False(t, trie.Search("app"))
	assert.True(t, trie.StartsWith("app"))
	trie.Insert("app")
	assert.True(t, trie.Search("app"))
}
