"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class Node:
    def __init__(self):
        self.end = False
        self.letters = {}

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.letters:
                curr.letters[char] = Node()
            curr = curr.letters[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dots(node, subword):
            curr = node
            for i in range(len(subword)):
                if subword[i] == ".":
                    for key in curr.letters.keys():
                        if dots(curr.letters[key], subword[i + 1:]):
                            return True
                    return False
                elif subword[i] not in curr.letters:
                    return False
                curr = curr.letters[subword[i]]
            if not curr.end:
                return False
            return True
        return dots(self.root, word)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)