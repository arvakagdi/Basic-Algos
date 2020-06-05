'''
Trie using Defaultdict

Defaultdict is a container like dictionaries present in the module collections.
Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict
never raises a KeyError. It provides a default value for the key that does not exists.
'''

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True



    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node.is_word

# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their','the']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
assert not word_trie.exists('th')
print('All tests passed!')