"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

class Node:
    def __init__(self):
        self.end = False
        self.letters = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.letters:
                curr.letters[letter] = Node()
            curr = curr.letters[letter]
        curr.end = True

    def remove(self, word):
        def remove_nodes(node, index):
            if index  == len(word):
                return True
            child = node.letters[word[index]]
            status = remove_nodes(child, index + 1)
            if status ==  True and not child.letters:
                del node.letters[word[index]]
            else:
                status = False
            return status
        remove_nodes(self.root, 0)
            

class Solution:
    def find_neighbors(self, row, column):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, column))
        if row < self.height - 1:
            neighbors.append((row + 1, column))
        if column > 0:
            neighbors.append((row, column - 1))
        if column < self.length - 1:
            neighbors.append((row, column + 1))
        return neighbors
    
    def find_word(self, row, column, node, tries):
        letter = self.board[row][column]
        if letter not in node.letters:
            return
        
        self.word.append(letter)
        self.visited.add((row, column))
        node = node.letters[letter]

        if node.end == True:
            word = ''.join(self.word)
            self.result.add(word)
            if not node.letters:
                tries.remove(word)

        neighbors = self.find_neighbors(row, column)
        for neighbor in neighbors:
            if neighbor not in self.visited:
                neighbor_row, neighbor_column = neighbor
                self.find_word(neighbor_row, neighbor_column, node, tries)
        
        self.word.pop()
        self.visited.remove((row, column))


    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):
        self.result = set()
        self.word = []
        self.visited = set()
        self.board = board

        trie = Trie()
        for word in words:
            trie.insert(word)

        self.height = len(board)
        self.length = len(board[0])

        for row in range(self.height):
            for column in range(self.length):
                self.find_word(row, column, trie.root, trie)
        
        return self.result



def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    solution = Solution()

    result = solution.findWords(board, words)
    
    print(result)


if __name__ == "__main__":
    main()