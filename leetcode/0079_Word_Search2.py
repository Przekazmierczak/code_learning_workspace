"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        ROWS = len(board)
        COLUMNS = len(board[0])
        WORD = len(word)
        
        def check_letters():
            letters = {}
            for letter in word:
                if letter not in letters:
                    letters[letter] = 0
                letters[letter] += 1

            for row in range(ROWS):
                for column in range(COLUMNS):
                    if board[row][column] in letters:
                        letters[board[row][column]] -= 1
                        if letters[board[row][column]] == 0:
                            del letters[board[row][column]]
                            if not letters:
                                return True
            return False
        
        def neighbor_cells(row, column):
            neighbors = []
            if row > 0:
                neighbors.append((row - 1, column))
            if row < ROWS - 1:
                neighbors.append((row + 1, column))
            if column > 0:
                neighbors.append((row, column - 1))
            if column < COLUMNS - 1:
                neighbors.append((row, column + 1))
            return neighbors
        
        def check(pointer, row, column):
            word_letter = word[pointer]
            board_letter = board[row][column]
            
            if board_letter != word_letter:
                return False
            
            if pointer == WORD - 1:
                return True
            
            board[row][column] = "."
            neighbors = neighbor_cells(row, column)
            
            for neighbor in neighbors:
                neighbor_row, neighbor_column = neighbor
                if check(pointer + 1, neighbor_row, neighbor_column):
                    return True
            board[row][column] = board_letter
            return False
        
        if not check_letters():
            return False
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if check(0, row, column):
                    return True
        return False 


def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "AS"

    solution = Solution()

    result = solution.exist(board, word)
    
    print(result)


if __name__ == "__main__":
    main()