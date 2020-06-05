'''
Checking if the word is valid using Trie
Trie decreases the use of memory as compared to HashMaps that would take O(n*m)
while sacrificing a little with performance

You can lookup a word by checking if word_end is True after traversing all the characters in the word.
Let's look at the word "hi". The first letter is "h", so you would call basic_trie['h'].
The second letter is "i", so you would call basic_trie['h']['i']. Since there's no more letters left,
you would see if this is a valid word by getting the value of word_end. Now you have basic_trie['h']['i']['word_end']
with True or False if the word exists.

In basic_trie, words "a" and "add" overlapp. This is where a Trie saves memory.
Instead of having "a" and "add" in different cells, their characters treated like nodes in a tree.
Let's see how we would check if a word exists in basic_trie.
'''


#look up dictionary
# words in our dictionary: a, add, hi

basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},    #is 'add' a word
            'word_end': False},         #is 'ad' a word
        'word_end': True},              # is 'a' a word
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False

        current_node = current_node[char]

    return current_node['word_end']


# Test words
test_words = ['ap', 'add','d']
for word in test_words:
    if is_word(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))